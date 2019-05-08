import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    TARANTOOL_HOST = os.environ.get('TARANTOOL_HOST') or 'localhost'
    TARANTOOL_PORT = os.environ.get('TARANTOOL_PORT') or '3301'

    POSTGRES_URI = os.environ.get('POSTGRES_URI') or 'postgres://postgres:postgres@localhost:5432/postgres'
    CLICKHOUSE_URI = os.environ.get('CLICKHOUSE_URI') or "clickhouse://default:@localhost:8123"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_BINDS = {
        'pgsql': POSTGRES_URI,
        'clickhouse': CLICKHOUSE_URI
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
