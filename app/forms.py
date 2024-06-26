from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user


# Определение класса RegistrationForm, наследующегося от FlaskForm
class RegistrationForm(FlaskForm):
    # Определение полей формы для регистрации пользователя
    username = StringField(  # Поле для ввода логина
        'Логин',
        validators=[DataRequired(),
        Length(min=2, max=35)])

    email = StringField(  # Поле для ввода почты
        'Почта',
        validators=[DataRequired(),
        Email()])

    password = PasswordField(  # Поле для ввода пароля
        'Пароль',
        validators=[DataRequired()])

    confirm_password = PasswordField(  # Поле для повторного ввода пароля
        'Повторите пароль',
        validators=[DataRequired(),
        EqualTo('password')])

    submit = SubmitField('Отправить')  # Кнопка отправки формы

    # Метод для валидации уникальности логина
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

    # Метод для валидации уникальности email
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Такая почта уже используется')


class LoginForm(FlaskForm):   # Определение класса LoginForm, наследующегося от FlaskForm
    # Определение полей формы для входа пользователя
    email = StringField('Email',     # Поле для ввода email
                        validators=[DataRequired(),
                        Email()])

    password = PasswordField('Пароль',
                             validators=[DataRequired()])  # Поле для ввода пароля

    remember = BooleanField('Запомни меня')  # Поле для запоминания пользователя

    submit = SubmitField('Отправить')  # Кнопка отправки формы


class UpdateProfileForm(FlaskForm):
    username = StringField(  # Поле для ввода нового имени
        'Новое имя',
        validators=[DataRequired(),
        Length(min=2, max=35)])

    email = StringField(  # Поле для ввода новой почты
        'Новая почта',
        validators=[DataRequired(),
        Email()])

    password = PasswordField(  # Поле для ввода нового пароля
        'Новый пароль',
        validators=[DataRequired()])

    confirm_password = PasswordField(  # Поле для повторного ввода нового пароля
        'Повторите новый пароль',
        validators=[DataRequired(),
        EqualTo('password')])

    submit = SubmitField('Сохранить изменения')  # Кнопка для сохранения изменений

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Это имя занято. Пожалуйста, выберите другое.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Этот адрес занят. Пожалуйста, выберите другой.')
