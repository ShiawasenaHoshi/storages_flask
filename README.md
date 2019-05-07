# Three storages in flask: pgsql, clickhouse, tarantool

## Code init
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Containers
```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
docker run -d --name clickhouse --ulimit nofile=262144:262144 -p 8123:8123 yandex/clickhouse-server
docker run --name tarantool -d -p 3301:3301 tarantool/tarantool:1
```
## Links
- [clickhouse db explorer in Idea](https://blog.magazov.com/clickhouse-intellij-idea/) 

- [clickhouse-sqlalchemy package](https://github.com/xzkostyan/clickhouse-sqlalchemy) 

- [multiple dbs in sqlalchemy](https://flask-appbuilder.readthedocs.io/en/latest/multipledbs.html) 

- [sqlalchemy+clickhouse create/drop table bug](https://github.com/xzkostyan/clickhouse-sqlalchemy/issues/22)  