import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST') or 'localhost'
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT') or '5432'
    POSTGRES_DB = os.environ.get('POSTGRES_DB') or 'postgres'
    POSTGRES_USER = os.environ.get('POSTGRES_USER') or 'postgres'
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD') or 'postgres'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  \
                              'postgres://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD\
                              + "@" + POSTGRES_HOST + ":" + POSTGRES_PORT + "/" + POSTGRES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TARANTOOL_HOST = os.environ.get('TARANTOOL_HOST') or 'localhost'
    TARANTOOL_PORT = os.environ.get('TARANTOOL_PORT') or '3301'
    TARANTOOL_USER = os.environ.get('TARANTOOL_USER') or 'tarantool'
    TARANTOOL_PASSWORD = os.environ.get('TARANTOOL_PASSWORD') or 'tarantool'

    CLICKHOUSE_URI = os.environ.get('CLICKHOUSE_URI') or "clickhouse://default:@localhost:8123"
    
