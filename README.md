![satus bage](https://github.com/kungfuproger/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Исходник: Групповой проект. 
Добавлено: загрузка из docker-compose, Action для автоматизации тестирования и деплоя на сервер.

# api_yamdb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title).
Произведения делятся на категории(Category).
У произведений есть жанры(Genres).

### Запуск приложения на сервере

1. Клонируйте этот репозиторий на сервер.

2. Для запуска потребуется установленное приложение Docker.
Ссылка для загрузки: https://www.docker.com/get-started/

3. Выполние настройки БД (Раздел ниже)

4. Строим контейнер Docker
```
# Из директории infra/
docker-compose up -d --build
```
5. Подгатавливаем элементы Django
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

6. Так можно загрузить в БД тестовые данные
```
docker-compose exec web python manage.py loaddata fixtures.json
```

7. Сайт доступен по адресу http://localhost/.

### Конфигурация БД 

1. Переименуйте файл `infra/.env.dist` в `.env`.
2. При необходимости установите собственные значения параметров в файле.
