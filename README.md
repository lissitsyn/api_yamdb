# API_YAMDB
API_YAMDB

API для доступа к проекту YaMDB. Создано для доступа сторонних приложений к проекту.
Позволяет выполнять запросы для взаимодействия с базой данных с разграниченим прав
в зависимости от роли пользователя.

**В проекте предусмотрены следующие роли:**

- суперпользователь (максимальные права доступа и редактирования)
- администратор
- модератор
- пользователь

Часть GET-запросов возможна без авторизации.

Авторизация происсходит по JWT-токену.

В проекте предусмотрена management-команда **load_data** для загрузки файлов в формате **csv** в БД через Django ORM. 
Инструкция по загрузке файлов описана после раздела с примерами запросов.

Со структурой БД можно ознакомиться по ссылке: https://dbdiagram.io/embed/62f224aac2d9cf52fa715ea5.

**Технологии:**

 - _[Python 3.7](https://docs.python.org/3/)_
 - _[Django 2.2.16](https://docs.djangoproject.com/en/2.2/)_
 - _[Django REST framework 3.12.4](https://www.django-rest-framework.org/)_
 - _[Simple JWT 4.7.1](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)_

**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AMRedichkina/api_yamdb 
cd api_yamdb
```

Cоздать и активировать виртуальное окружение
(инструкция дана для систем на базе ОС Windows):

```
python -m venv env
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Загрузить встроенную базу данных:

```
cd api_yamdb
python manage.py load_data 
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

# Примеры запросов.

Создание учетной записи.

POST
```
/api/v1/auth/signup/
```

BODY
```
{
"email": "user@user.uu",
"username": "user1"
}
```

RESPONSE
```
{
"email": "user@user.uu",
"username": "user1"
}
```


Получение JWT-токена.

POST
```
/api/v1/auth/token/
```

BODY
```
{
"username": "user1",
"confirmation_code": "1176"
}
```

RESPONSE
```
{
"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNTg0MzM2LCJpYXQiOjE2NjAyODgzMzYsImp0aSI6ImJmMTRkNjAxZWRmOTQ3ZTBiYTczZTg2Yjk4NDY1ODQxIiwidXNlcl9pZCI6MTA3fQ.RRz6DPnN8EvMFrla-s6oysMiEYOqY0mzv1-xkUmoZqY"
}
```


Получение списка категорий.

GET
```
/api/v1/categories/
```

RESPONSE
```
[
    {
        "count": 16,
        "next": "http://127.0.0.1:8000/api/v1/categories/?page=2",
        "previous": null,
        "results": [
            {
            "name": "category1",
            "slug": "category1"
            }
        ...
        ]
    }
]
```


Создание новой категории.

POST
```
/api/v1/categories/
```

BODY
```
{
    "name": "category6",
    "slug": "category6"
}
```

RESPONSE
```
{
    "name": "category6",
    "slug": "category6"
}
```


Удаление категории.

DELETE
```
/api/v1/categories/category7/
```

RESPONSE
```

```


Получение списка жанров.

GET
```
/api/v1/genres/
```

RESPONSE
```
{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/v1/genres/?page=2",
    "previous": null,
    "results": [
        {
            "name": "genre10",
            "slug": "genre10"
        },
        ...
        ]
    }
]
```


Создание нового жанра.

POST
```
/api/v1/genres/
```

BODY
```
{
    "name": "genre6",
    "slug": "genre6"
}
```

RESPONSE
```
{
    "name": "genre6",
    "slug": "genre6"
}
```


Удаление жанра.

DELETE
```
/api/v1/genres/genre7/
```

RESPONSE
```

```


Получение списка произведений.

GET
```
/api/v1/titles/
```

RESPONSE
```
{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/v1/titles/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "title1",
            "year": 2001,
            "rating": null,
            "description": null,
            "genre": [
                {
                    "name": "genre6",
                    "slug": "genre6"
                }
            ],
            "category": {
                "name": "category1",
                "slug": "category1"
            }
        },
        ...
        ]
    }
]
```


Создание нового произведения.

POST
```
/api/v1/titles/
```

BODY
```
{
    "name": "title7",
    "year": "2007",
    "genre": ["genre6"],
    "category": "category1"
}
```

RESPONSE
```
{
    "id": 7,
    "name": "title7",
    "year": 2007,
    "rating": null,
    "description": null,
    "genre": [
        "genre6"
    ],
    "category": "category1"
}
```


Получение информации о произведении.

GET
```
/api/v1/titles/3/
```

RESPONSE
```
{
    "id": 3,
    "name": "title3",
    "year": 2003,
    "rating": null,
    "description": null,
    "genre": [
        {
            "name": "genre6",
            "slug": "genre6"
        }
    ],
    "category": {
        "name": "category1",
        "slug": "category1"
    }
}
```


Частичное обновление информации о произведении.

PATCH
```
/api/v1/titles/3/
```

BODY
```
{
    "category": "category2"
}
```

RESPONSE
```
{
    "id": 3,
    "name": "title3",
    "year": 2003,
    "rating": null,
    "description": null,
    "genre": [
        "genre6"
    ],
    "category": "category2"
}
```


Удаление произведения.

DELETE
```
/api/v1/titles/3/
```

RESPONSE
```

```


Получение списка ревью.

GET
```
/api/v1/titles/3/reviews/
```

RESPONSE
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "title3",
            "author": "New user6",
            "text": "review",
            "score": 5,
            "pub_date": "2022-08-15T12:35:28.363020Z"
        }
    ]
}
```


Создание нового ревью.

POST
```
/api/v1/titles/3/reviews/
```

BODY
```
{
    "text": "review",
    "score": "5"
}
```

RESPONSE
```
{
    "id": 1,
    "title": "title3",
    "author": "New user6",
    "text": "review",
    "score": 5,
    "pub_date": "2022-08-15T12:35:28.363020Z"
}
```


Получение информации о ревью.

GET
```
/api/v1/titles/3/reviews/1/
```

RESPONSE
```
{
    "id": 1,
    "title": "title3",
    "author": "New user6",
    "text": "review",
    "score": 5,
    "pub_date": "2022-08-15T12:35:28.363020Z"
}
```


Частичное обновление информации о ревью.

PATCH
```
/api/v1/titles/3/reviews/1/
```

BODY
```
{
    "score": "7"
}
```

RESPONSE
```
{
    "id": 1,
    "title": "title3",
    "author": "New user6",
    "text": "review",
    "score": 7,
    "pub_date": "2022-08-15T12:35:28.363020Z"
}
```


Удаление ревью.

DELETE
```
/api/v1/titles/3/reviews/1/
```

RESPONSE
```

```


Получение списка комментариев.

GET
```
/api/v1/titles/3/reviews/1/comments/
```

RESPONSE
```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "New user6",
            "pub_date": "2022-08-15T12:39:39.829425Z",
            "text": "Comment1"
        },
        {
            "id": 2,
            "author": "New user6",
            "pub_date": "2022-08-15T12:39:43.793169Z",
            "text": "Comment2"
        },
        {
            "id": 3,
            "author": "New user6",
            "pub_date": "2022-08-15T12:39:46.032140Z",
            "text": "Comment3"
        }
    ]
}
```


Создание нового комментария.

POST
```
/api/v1/titles/3/reviews/1/comments/
```

BODY
```
{
    "text": "comment1",
}
```

RESPONSE
```
{
    "id": 1,
    "author": "New user6",
    "pub_date": "2022-08-15T12:39:39.829425Z",
    "text": "Comment1"
}
```


Получение информации о комментарии.

GET
```
/api/v1/titles/3/reviews/1/comments/1/
```

RESPONSE
```
{
    "id": 1,
    "author": "New user6",
    "pub_date": "2022-08-15T12:39:39.829425Z",
    "text": "Comment1"
}
```


Частичное обновление информации о ревью.

PATCH
```
/api/v1/titles/3/reviews/1/comments/1/
```

BODY
```
{
    "text": "new text"
}
```

RESPONSE
```
{
    "id": 1,
    "author": "New user6",
    "pub_date": "2022-08-15T12:39:39.829425Z",
    "text": "New text"
}
```


Удаление комментария.

DELETE
```
/api/v1/titles/3/reviews/1/comments/1/
```

RESPONSE
```

```


Получение списка пользователей.

GET
```
/api/v1/auth/users/
```

RESPONSE
```
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/v1/users/?page=2",
    "previous": null,
    "results": [
        {
            "username": "New user",
            "email": "email@shitmail.gov",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        ...        
    ]
}
```


Создание нового пользователя.

POST
```
/api/v1/users/
```

BODY
```
{
    "username": "user111",
    "email": "user111@usermail.au"
}
```

RESPONSE
```
{
    "username": "user111",
    "email": "user111@usermail.au",
    "first_name": "",
    "last_name": "",
    "bio": "",
    "role": "user"
}
```


Получение пользователя по username.

GET
```
/api/v1/users/user111/
```

RESPONSE
```
{
    "username": "user111",
    "email": "user111@usermail.au",
    "first_name": "",
    "last_name": "",
    "bio": "",
    "role": "user"
}
```


Изменение данных пользователя.

PATCH
```
/api/v1/users/user111/
```

BODY
```
{
    "bio": "biorobot"
}
```

RESPONSE
```
{
    "username": "user111",
    "email": "user111@usermail.au",
    "first_name": "",
    "last_name": "",
    "bio": "biorobot",
    "role": "user"
}
```


Удаление пользователя.

DELETE
```
/api/v1/users/user111/
```

RESPONSE
```

```


Получение данных о своей учетной записи.

GET
```
/api/v1/users/me/
```

RESPONSE
```
{
    "username": "New user6",
    "email": "email@shitmail6.gov",
    "first_name": "",
    "last_name": "",
    "bio": "biorobot",
    "role": "admin"
}
```


Изменение данных своей учетной записи.

PATCH
```
/api/v1/users/me/
```

BODY
```
{
    "bio": "my bio"
}
```

RESPONSE
```
{
    "username": "New user6",
    "email": "email@shitmail6.gov",
    "first_name": "",
    "last_name": "",
    "bio": "my bio",
    "role": "admin"
}
```

# Загрузка в базу данных сведений из файлов CSV через Django ORM

*Набор необходимых файлов*

Для загрузки данных в БД вам необходимо, сгрупировать в директории файлы со следующими именами:

- category.csv (данные о категориях)
- genre.csv (данные о жанрах)
- titles.csv (данные о произведениях)
- users.csv (данные о пользователях)
- genre_title.csv (данные о связи произведения и его жанра)
- review.csv (данные об отзывах)
- comments.csv (данные о комментариях)

## Требования к полям файлов
Ниже вы найдёте минимальный набор полей необходимый в каждом файле чтобы загрузка прошла успешно.

#### * **category.csv** *(данные о категориях)*
| *id*        | *name*          | *slug* |
|:----------:|:-------------:| :-----:|
| 1      | Фильм | film |
| 2      | Книга | book |

#### * **genre.csv** *(данные о жанрах)*
| *id*        | *name*           | *slug* |
| :-------------: |:-------------:|:-----:|
| 1      | Драма | drama |
| 2      | Комедия | comedy |

#### * **titles.csv** *(данные о произведениях)*
| *id*  | *name*          | *year* | *category_id* | *description* |
|:---:|:-------------:|:-----:|:-----:|:-----:|
| 1   | Колобок | 1873 | 2 | A ball of bread |
| 2   | Назад в будущее | 1985 | 1 |  |

#### * **users.csv** *(данные о пользователях)*
| *id*  | *username*          | *email* | *role* | *first_name* | *last_name* | 
|:---:|:-------------:|:-----:|:-----:|:-----:|:-------|
| 100   | spider | sppitpark@aveng.com | user | Piter | Parker  |
| 101   | VolanDeMort | slizerin@hogwarts.com | admin |  |     |

#### * **genre_title.csv** *(данные о связи произведения и его жанра)*
| *id*        | *title_id*          | *genre_id* |
|:----------:|:-------------:| :-----:|
| 1      | 1 | 1 |
| 2      | 2 | 1 |

#### * **review.csv** *(данные об отзывах)*
| *id*  | *title_id*          | *text* | *author_id* | *score* | *pub_date* | 
|:---:|:-------------:|:-----:|:-----:|:-----:|:-------:|
| 1   | 1 | This was amazing | 100| 10 | 2019-09-24T21:08:21.567Z  |
| 2   | 1 | Avada Kedavra | 101 | 1 |  2019-09-24T21:08:21.567Z   |

#### * **comments.csv** *(данные о комментариях)*
| *id*  | *review_id*          | *text* | *author_id* | *pub_date* | 
|:---:|:-------------:|:-----:|:-----:|:-------:|
| 1   | 1 | Bullshit | 70 |2019-09-24T21:08:21.567Z  |
| 2   | 6 | Lumus | 60 |2019-09-24T21:08:21.567Z   |

## Загрузка данных

Загрузить данные можно используя команду

```shell
python3 manage.py load_data
```

*Комментарий: в передаваемых данных есть связанны поля. Будьте внимательны, рекомендуем предварительно ознакомиться со структурой БД*

## Авторы проекта:
- Лисицын Вячеслав
- Редичкина Александра