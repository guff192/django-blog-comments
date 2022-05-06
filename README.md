# django-blog-comments
### Для запуска приложения:
```
make run
```
Если приложение запускается впервые, необходимо сначала собрать образ, а также создать базу данных и применить к ней миграции после успешного запуска:
```
make build && make run
make createdb && make migrate
```

Для остановки:
```
make stop
```