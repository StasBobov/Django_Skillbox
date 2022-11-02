# создать каркас и файлы для работы приложения
django-admin startproject todo
# табличку какую-то выводит
ls
# перейти в директорию проекта 'todo'
cd todo/
# создаём новое приложение (создаёт папку tasks)
django-admin startapp tasks
# миграция данных в базу данных (создаёт файл manage.py)
python manage.py migrate
# создаём пользователя
python manage.py createsuperuser
# запускаем сервер
python manage.py runserver
# остановить сервер
CTRL + C
