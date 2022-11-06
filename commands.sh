# создаём папку с виртуальным окружением
pip freeze > requairements.txt


# создать каркас и файлы для работы приложения
django-admin startproject todo
# табличку какую-то выводит
ls
# перейти в директорию проекта 'todo'
cd todo/


# создаём пользователя
python manage.py createsuperuser
# запускаем сервер
python manage.py runserver
# остановить сервер
CTRL + C

'''Работа с проектом'''
# создание проекта 'board'
django-admin startproject board
# посмотреть дерево проекта board
tree board
# справка
python manage.py help
python manage.py help startapp
# создаём структуру приложения django в папке с именем advertisement
python manage.py startapp advertisement
# создание базы данных (набор таблиц и связи между ними из базового пакета django SQLite)
python manage.py migrate