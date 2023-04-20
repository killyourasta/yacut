# YaCut
Сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса:
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.
Доступны web и api интерфейсы.

## Технологии
- Python 3.7
- Flask 2.0
- Jinja2 3.0
- SQLAlchemy 1.4
## Использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/killyourasta/yacut.git
```
```
cd yacut
```
Создать файл .env Пример:
```
FLASK_APP=yacut
FLASK_ENV= # development - если приложение в разработке
					  # production - если приложение полностью готово
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
Если у вас Linux/macOS
```
source venv/bin/activate
```
Если у вас windows

```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:

```
flask db upgrade
```
Запуск проекта:

```
flask run
```
Автор: [Ляйсан Галиева](https://github.com/killyourasta)
