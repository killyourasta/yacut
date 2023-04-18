import os
import re

#Global
SHORT_ID_LENGTH = int(os.getenv('SHORT_ID_LENGTH', 6))
CUSTOM_ID_CHECK_RE = re.compile('[a-zA-Z0-9]+$')

#Forms
CHECK_RE_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
LENGTH_ERROR_MESSAGE = 'Длина ссылки не может быть больше 16 символов'
DESCRIPTION_URL = 'Длинная ссылка'
MISSING_DATA = 'Обязательное поле'
DESCRIPTION_SHORT = 'Ваш вариант короткой ссылки'

#Views
NOT_UNIQUE_LINK_MESSAGE = 'Имя {} уже занято!'

#Api_views
URL_CHECK_RE = re.compile(
    r'[A-Za-z0-9]+://[A-Za-z0-9%-_]+(/[A-Za-z0-9%-_])*(#|\\?)[A-Za-z0-9%-_&=]*'
)
MISSING_REQUEST = 'Отсутствует тело запроса'
REQUEST_NO_URL_MESSAGE = '"url" является обязательным полем!'
REQUEST_INV_URL_MESSAGE = 'Указана не ссылка'
ID_NOT_FREE = 'Имя "{}" уже занято.'
ERROR_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
NOT_FOUND_ID = 'Указанный id не найден'
