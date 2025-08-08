# 📡 Проект «API для YaTube»
**API-сервер для социальной платформы YaTube.**  
Учебный проект по созданию backend-приложения блога с возможностью создания своего личного блога,  
комментрирования постов, группировки постов по тематикам и подписок на авторов постов.   
   
API реализован на Django Rest Framework и осуществляет все необходимые функции приложения.   
Аутентификация осуществляется по JWT-токену.   

---

## 🔧 Возможности API

- **Регистрация и авторизация** через JWT
- **Публикация постов**
- **Комментарии** к постам
- **Группы** (категории) для постов
- **Подписка** на авторов
- **Постраничная пагинация**
- **Доступ через токен**: только автор может редактировать/удалять свой контент

---

## 🔗 Эндпоинты

| Метод | URL | Описание |
|--------|-----|----------|
| `POST` | `/api/v1/jwt/create/` | Получение JWT-токена |
| `POST` | `/api/v1/jwt/refresh/` | Обновление JWT-токена |
| `GET` | `/api/v1/posts/` | Список всех постов |
| `POST` | `/api/v1/posts/` | Создать новый пост |
| `GET` | `/api/v1/posts/{id}/` | Получить пост по ID |
| `PUT/PATCH` | `/api/v1/posts/{id}/` | Обновить пост |
| `DELETE` | `/api/v1/posts/{id}/` | Удалить пост |
| `GET` | `/api/v1/groups/` | Получить список групп |
| `GET` | `/api/v1/groups/{id}/` | Получить группу по ID |
| `GET/POST` | `/api/v1/posts/{post_id}/comments/` | Список/создание комментариев |
| `GET/PUT/DELETE` | `/api/v1/posts/{post_id}/comments/{id}/` | Работа с комментарием |
| `GET/POST` | `/api/v1/follow/` | Список подписок / подписка на автора |

> 📘 Подробная спецификация — Redoc: `/redoc/`

---

## 👨‍💻 Технологии

- Python 3.9+
- Django 3.2
- Django REST Framework
- Pytest
- JWT Auth (SimpleJWT)
- Postman

---

## 🚀 Запуск проекта
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Iceberen/api_final_yatube.git
    cd api_final_yatube

2. Cоздать и активировать виртуальное окружение:
    ```
    python -m venv venv
    source venv/bin/activate     # для Linux/macOS
    venv\Scripts\activate        # для Windows

3. Установить зависимости из файла requirements.txt:
    ```
    pip install -r requirements.txt

4. Выполните миграции и запустите сервер:
    ```
    python3 manage.py migrate
    python3 manage.py runserver     # для Linux/macOS
    python manage.py migrate
    python manage.py runserver      # для Windows

5. Тестирование Postman:
- Используйте коллекцию из postman_collection/API_for_yatube.postman_collection.json
- Настройка данных — postman_collection/set_up_data.sh

---

## 🧪 Тестирование
Тесты расположены в директории tests/.
Для запуска:
  ```
  pytest
  ```
Покрытие тестами:
- Авторизация (JWT)
- CRUD для постов, комментариев, подписок, групп
- Проверка прав доступа и ограничений

---

## 📬 Postman
Коллекция для тестирования API с примерами запросов:
  ```
  postman_collection/API_for_yatube.postman_collection.json
  ```
Файл `set_up_data.sh` поможет автоматически зарегистрировать пользователей и создать тестовые посты.

---

## 📁 Структура проекта
```
├── yatube_api/
│ ├── api/              # Эндпоинты и логика API (ViewSet’ы, сериализаторы, права доступа)
│ ├── posts/            # Приложение с моделями: Post, Comment, Group, Follow
│ ├── static/           # Cпецификация API Redoc
│ ├── yatube_api/       # Настройки Django
│ └── manage.py
├── tests/                  # Автотесты с использованием pytest
├── postman_collection/     # Коллекция запросов Postman
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧑‍💻 Автор
Разработано: [Iceberen](https://github.com/Iceberen) в рамках учебного спринта по DRF.

---