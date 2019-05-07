# storages_flask

```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
docker run -d --name clickhouse --ulimit nofile=262144:262144 -p 8123:8123 yandex/clickhouse-server
```

https://blog.magazov.com/clickhouse-intellij-idea/
https://github.com/xzkostyan/clickhouse-sqlalchemy
https://flask-appbuilder.readthedocs.io/en/latest/multipledbs.html
https://github.com/xzkostyan/clickhouse-sqlalchemy/issues/22 sqlalchemy+clickhouse create/drop table bug 