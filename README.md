# adminlte

Для поднятия проекта:

В вируальном окружении:

pip install -r requirements.txt

Демо данные для проекта в файле proceeds_dump.json.
Команда для устновки демо данных:

./manage.py migrate

./manage.py loaddata proceeds_dump.json

Запуск сервера:

./manage.py runserver

Чтобы войти в административную часть, необходимо создать админа:

./manage.py createsuperuser

