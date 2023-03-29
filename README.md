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

### Регистрация нового пользователя
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.
Использовать имя 'me' в качестве username запрещено.
Поля email и username должны быть уникальными.

*   `POST: /api/v1/auth/signup/
Content-Type: application/json

        {
        "email": "string",
        "username": "string"
        }


### Получение JWT-токена в обмен на username и confirmation code.
    
*   `POST: /api/v1/auth/token/
Content-Type: application/json

        {
        "username": "string",
        "confirmation_code": "string"
        }


### API
# Эндпоинты:
 CATEGORIES
 
`/api/v1/categories/`

 GENRES
 
`/api/v1/genres/`

 TITLES
 
`/api/v1/titles/`

`/api/v1/titles/{titles_id}/`

 REVIEWS
 
`/api/v1/titles/{title_id}/reviews/`

`/api/v1/titles/{title_id}/reviews/{review_id}/`

 COMMENTS
 
`/api/v1/titles/{title_id}/reviews/{review_id}/comments/`

`/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`

 USERS
 
`/api/v1/users/`

`/api/v1/users/{username}/`

Полная информация по запросам доступна в документации: `/redoc/`


### Management-команда import_csv

`python manage.py import_csv` - импортировать все файлы из директории static/data/

`python manage.py import_csv <filename>` - импортировать выбранный файл, можно импортировать сразу несколько выбранных фалов перечислив их имена через пробел.
