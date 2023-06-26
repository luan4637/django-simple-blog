The simple blog application that is using the Django framework.

# install
pip install Django
pip install mysqlclient
pip install Pillow

# create database
CREATE DATABASE djangoblog_db CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'djangoblog_user'@'localhost' IDENTIFIED BY 'djangoblog_password';
GRANT ALL PRIVILEGES ON djangoblog_db.* TO 'djangoblog_user'@'localhost';

# insert data sample: login mysql and run
source {application-directory}/data-sample.sql;

# migrate
python manage.py makemigrations
python manage.py migrate

# create super user
python manage.py createsuperuser

# run server
python manage.py runserver
