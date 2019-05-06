import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST') or 'localhost'
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT') or '5432'
    POSTGRES_USER = os.environ.get('POSTGRES_USER') or 'postgres'
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD') or 'postgres'
    TARANTOOL_HOST = os.environ.get('TARANTOOL_HOST') or 'localhost'
    TARANTOOL_PORT = os.environ.get('TARANTOOL_PORT') or '3301'
    TARANTOOL_USER = os.environ.get('TARANTOOL_USER') or 'tarantool'
    TARANTOOL_PASSWORD = os.environ.get('TARANTOOL_PASSWORD') or 'tarantool'
    CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST') or 'localhost'
    CLICKHOUSE_PORT = os.environ.get('CLICKHOUSE_PORT') or '8123'
    CLICKHOUSE_USER = os.environ.get('CLICKHOUSE_USER') or 'clickhouse'
    CLICKHOUSE_PASSWORD = os.environ.get('CLICKHOUSE_PASSWORD') or 'clickhouse'
    
