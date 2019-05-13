# Three storages in flask: pgsql, clickhouse, tarantool

Asynctnt not integrated with flask

## Code init
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Containers
For the first time
```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
docker run -d --name clickhouse --ulimit nofile=262144:262144 -p 8123:8123 yandex/clickhouse-server
docker run --name tarantool -p 3301:3301 -d -v /path/to/project/storages_flask:/opt/tarantool tarantool/tarantool tarantool /opt/tarantool/tnt_conf.lua
```
stop/start after
```bash
docker stop postgres clickhouse tarantool
docker start postgres clickhouse tarantool
```

## Links
- [clickhouse db explorer in Idea](https://blog.magazov.com/clickhouse-intellij-idea/) 

- [clickhouse-sqlalchemy package](https://github.com/xzkostyan/clickhouse-sqlalchemy) 

- [multiple dbs in sqlalchemy](https://flask-appbuilder.readthedocs.io/en/latest/multipledbs.html) 

- [sqlalchemy+clickhouse create/drop table bug](https://github.com/xzkostyan/clickhouse-sqlalchemy/issues/22)
  
- [attaching to tarantool](https://www.tarantool.io/ru/doc/2.1/book/getting_started/using_docker/#attaching-to-tarantool)

- [useless tarantool python connector manual (data types not found, wrong library interface)](https://tarantool-python.readthedocs.io/en/latest/quick-start.en.html)

- [asynctnt - fast python lib, but examples not worked for me out of the box](https://github.com/igorcoding/asynctnt)

- [python tarantool queue based on asynctnt](https://github.com/tarantool/queue-python)

- [Idea+lua+tarantool](https://www.tarantool.io/ru/doc/1.10/book/app_server/using_ide/)