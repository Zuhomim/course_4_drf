# Напоминание привычек в телеграм

## Используемый framework: Docker, Django, Redis, PostgreSQL.

# Инструкция по установке и запуску

## Docker
https://docs.docker.com/get-docker/

## PostgreSQL
https://www.postgresql.org/download/

## Redis
https://redis.io/download/

## Docker-Compose (подготовка и запуск контейнера)

### Соберите образ с помощью команды:
```docker-compose build```

### Запуск контейнеров:
```docker-compose up```

### Остановка контейнеров:
```docker-compose down```

### Перезапуск контейнеров:
```docker-compose restart```

### Загрузка последних версий образов для сервисов файла docker-compose.yaml:
```docker-compose pull```

[//]: # (## Установка:)

[//]: # (### 1. Fork репозитория )

[//]: # (#### https://github.com/Zuhomim/course_4_drf)

[//]: # (### 2. Установка зависимостей из файла requirements)

[//]: # (```pip install -r requirements.txt```)

[//]: # (### 3. Создайте файл .env в корневой директории &#40;согласно шаблону .env.template&#41;)

[//]: # (### 4. Установите redis:)

[//]: # (#### https://redis.io/docs/install/install-redis/)

[//]: # ()
[//]: # (## Запуск:)

[//]: # (### 1. Выполняем команду в терминале &#40;redis должен быть запущен&#41;)

[//]: # (```python manage.py runserver```)

[//]: # (### 2. Запускаем celery для периодических задач)

[//]: # (```celery -A my_project worker —loglevel=info```)

[//]: # (```celery -A my_project beat —loglevel=info```)