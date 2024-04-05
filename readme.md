# Напоминание привычек в телеграм

## Используемый framework: Django, PostgreSQL.

## Установка:
### 1. Fork репозитория 
#### https://github.com/Zuhomim/course_4_drf
### 2. Установка зависимостей из файла requirements
```pip install -r requirements.txt```
### 3. Создайте файл .env в корневой директории (согласно шаблону .env.template)
### 4. Установите redis:
#### https://redis.io/docs/install/install-redis/

## Запуск:
### 1. Выполняем команду в терминале (redis должен быть запущен)
```python manage.py runserver```
### 2. Запускаем celery для периодических задач
```celery -A my_project worker —loglevel=info```
```celery -A my_project beat —loglevel=info```