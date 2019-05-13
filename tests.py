import asyncio
import unittest
from datetime import timedelta, date

from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from app import create_app, db
from app.models import Place, User, Rate
from atnt import queue_usage
from config import Config



class TestConfig(Config):
    TESTING = True


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all(bind='pgsql')

    def tearDown(self):
        db.session.remove()
        db.drop_all(bind='pgsql')
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_add_users(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()


class RateModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all(bind='clickhouse')

    def test_insert_rate(self):
        today = date.today()
        rates = [Rate(day=today - timedelta(i), value=200 - i) for i in range(100)]
        db.session.add_all(rates)
        db.session.commit()

    def tearDown(self):
        # todo workaround for clickhouse + sqlalchemy https://github.com/xzkostyan/clickhouse-sqlalchemy/issues/22
        ch = db.make_connector(self.app, bind='clickhouse').get_engine()
        Session = sessionmaker(ch)
        session = Session()
        meta = MetaData(ch, reflect=True)
        for table in reversed(meta.sorted_tables):
            session.execute("drop table " + table.name)
        self.app_context.pop()


class PlaceModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_crud(self):
        place1 = Place("USA", "United states of America")
        place1.save()
        place_found = Place.search("USA")
        self.assertEqual(place1, place_found)
        Place.delete(place1)
        place_not_found = Place.search("USA")
        self.assertIsNone(place_not_found)


class AsyncTNTCase(unittest.TestCase):
    loop = asyncio.get_event_loop()

    def tearDown(self):
        self.loop.close()

    def test_queue(self):
        self.loop.run_until_complete(queue_usage())


if __name__ == '__main__':
    unittest.main(verbosity=2)
