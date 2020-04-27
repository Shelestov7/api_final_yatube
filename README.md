

## Реализация API на базе Django Rest Framework

##### Для запуска проекта необходимо:

Установить зависимости:

`pip install -r requirements.txt`

Создать модели:

`python manage.py makemigrations`

Провести миграцию:

`python manage.py migrate`

Запустить сервер командой:

`python manage.py runserver`

##### Доступные методы:

`/api/v1/posts/  (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>  (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments/<id> (GET, POST, PUT, PATCH, DELETE)
/api/v1/group/  (GET, POST)
/api/v1/follow/ (GET, POST)`

##### Для доступа к API необходимо получить токен:

Небходимо сздать POST-запрос `localhost:8000/api/v1/token/` передав поля **username** и **password**. API вернет токен.