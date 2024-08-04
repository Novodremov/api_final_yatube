# **API_final_Yatube**
API для работы с постами сервиса Yatube, предоставляет доступ для чтения публикаций и комментариев всем пользователям, авторизованным пользователям позволяет публиковать новые посты и комментарии и редактировать свои существующие. Внедрены системы сообществ и подписок.
## Использованные технологии:
Проект написан на Python, с использованием фреймворков Django и Django REST Framework.
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Novodremov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Перейти в директорию управления проектом:
```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
# Доступные эндпоинты:
### Любой пользователь может:
 - получить список всех публикаций; при указании параметров limit и offset выдача должна работать с пагинацией
```
GET /api/v1/posts/
```
- получить публикацию по id
``` 
GET /api/v1/posts/{id}/
```
- получить список доступных сообществ
```
GET /api/v1/groups/
```
- получить информацию о сообществе по id
```
GET /api/v1/groups/{id}/
```
- получить все комментарии к публикации
```
GET /api/v1/{post_id}/comments/
```
- получить комментарий к публикации по id
```
GET /api/v1/{post_id}/comments/{id}/
```
### Аутентифицированный пользователь может:
- создать новую публикацию
```
POST /api/v1/posts/
```
#### **Пример:**
__*Запрос:*__
{
  "text": "string",
  "image": "string",
  "group": 0
}
__*Ответ:*__
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
- обновить (в т.ч. частично) и удалить свою существующую публикацию
```
PUT /api/v1/posts/{id}/
PATCH /api/v1/posts/{id}/
DEL /api/v1/posts/{id}/
```
- оставить комментарии
```
POST /api/v1/posts/{post_id}/comments/)
```
#### **Пример:**
__*Запрос:*__
{
  "text": "string"
}
__*Ответ:*__
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
- обновить (в т.ч. частично) и удалить свой существующий комментарий
```
PUT /api/v1/posts/{post_id}/comments/{id}/)
PATCH /api/v1/posts/{post_id}/comments/{id}/)
DEL /api/v1/posts/{post_id}/comments/{id}/)
```
- получить список своих подписок
```
GET /api/v1/follow/
```
- подписаться на пользователя  
```
POST /api/v1/follow/
```
#### **Пример:**
__*Запрос:*__
{
  "following": "string"
}
__*Ответ:*__
{
  "user": "string",
  "following": "string"
}
- получить новый JWT-токен  
```
POST /api/v1/jwt/create/
```
#### **Пример:**
__*Запрос:*__
{
  "username": "string",
  "password": "string"
}
__*Ответ:*__
{
  "refresh": "string",
  "access": "string"
}
- обновить JWT-токен
```
POST /api/v1/jwt/refresh/
```
- проверить JWT-токен
```
POST /api/v1/jwt/verify/
```

## Авторы:
Яндекс-Практикум и Алексей Лысов