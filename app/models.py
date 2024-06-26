from app import db, login_manager  # Импорт объектов db и login_manager из пакета app
from flask_login import UserMixin  # Импорт класса UserMixin из пакета flask_login

# Функция, которая загружает пользователя по его идентификатору
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):  # Определение класса User, наследующегося от db.Model и UserMixin
    # Определение полей таблицы пользователей
    id = db.Column(db.Integer, primary_key=True)  # Первичный ключ
    username = db.Column(db.String(20), unique=True, nullable=False)  # Имя пользователя
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email пользователя
    password = db.Column(db.String(60), nullable=False)  # Пароль пользователя

    # Метод для представления объекта класса User в виде строки
    def repr(self):
        return f'User: {self.username}, email: {self.email}'
