# Проект "Парсер задач"

## Краткое описание

Парсер, который получает данные по задачам с сайта codeforces.com и записывает в базу данных. Проект выполнен на
Windows.
Создан с использованием Python и Django REST framework. Настроен вывод документации
через Redoc, реализовано асинхронное выполнение задач с помощью Celery. В качестве брокера
используется Redis, в качестве базы данных PostgreSQL. Также в проекте имеется интеграция Telegram для подбора задач по
сложности и теме и формирования контеста из 10 задач.

## Инструкция по запуску

1. Создайте файл .env по образцу в файле .env.sample.
2. Установите зависимости проекта, указанные в файле requirements.txt.
3. Установите redis (ссылка на пакет для Windows: https://github.com/microsoftarchive/redis/releases).
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. Выполните миграции

   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

6. Для запуска асинхронных задач необходимо запустить Celery и Celery-beat
    ```bash
    celery -A config worker -P eventlet -l INFO 
   ```

   ```bash
    celery -A config beat -l info -S django 
   ```
7. Для запуска Telegram-bot выполнить команду
   ```bash
    python manage.py telegram_bot
   ```

## Технологии в проекте (стек)

* Python 3.11
* Django
* DRF
* PostgreSQL
* Celery
* Redis
* Unittest
* flake8
