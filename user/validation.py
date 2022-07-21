import re

from django.core.exceptions import ValidationError

def signup_user_name(user_name):
    REGEX_USER_NAME = '^[a-zA-Z0-9]{4,16}$'
    if not re.match(REGEX_USER_NAME, user_name):
        raise ValidationError("ID_ERROR")

def signup_email(email):
    REGEX_EMAIL  = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError("EMAIL_ERROR")

def signup_password(password):
    REGEX_PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()])[A-Za-z\d~!@#$%^&*()]{8,16}'
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError("PASSWORD_ERROR")