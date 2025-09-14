<h1 align="center">
  <img src="resources/images/preview.png" align="top" alt="Logo">
</h1>

<h1 align="center">
    
  SUAI Deadline Bot 🤖🔥

  ![Python](https://custom-icon-badges.demolab.com/badge/3.10+-ff480d?logo=pythonn&label=Python)
  ![aiogram](https://img.shields.io/badge/aiogram-3.x-ff480d?style=flat&logo=telegram)
  ![SQLAlchemy](https://custom-icon-badges.demolab.com/badge/2.0-ff480d?logo=sqlalchemy&label=SQLAlchemy)
  [![License](https://custom-icon-badges.demolab.com/badge/MIT-ff480d?logo=law&label=License)](LICENSE)
  
</h1>

Телеграм-бот для студентов ГУАП, который автоматически отслеживает дедлайны в личном кабинете и присылает уведомления. Проект выполнен в рамках <b><i>учебной практики</i></b>🎓.

## ✨ Основные возможности

*   **🔍 Автоматический парсинг ЛК:** Бот самостоятельно заходит в личный кабинет `pro.guap.ru` и собирает актуальные дедлайны.
*   **🔔 Гибкие уведомления:**
    *   **Ежедневные:** Напоминания за 1, 3 или 7 дней до сдачи.
    *   **Частые:** Возможность получать дедлайны каждые N часов.
*   **🎨 Персонализация:** Пользователь может включать/выключать уведомления и настраивать их частоту.
*   **🙋🏻‍♂️ Кастомные дедлайны:** Возможность добавлять и удалять собственные (личные дедлайны), которые не связаны с ЛК.
*   **🔐 Безопасность:** Все учетные данные (логин, пароль) хранятся в базе данных в зашифрованном виде.
*   **📲 Удобный интерфейс:** Управление через команды и интерактивные inline-кнопки.

## 🛠 Технологический стек

*   **Язык:** [Python 3.12.5](https://www.python.org/downloads/release/python-3125)
*   **Асинхронный фреймворк:** [asyncio](https://docs.python.org/3/library/asyncio.html)
*   **Telegram Bot API:** [aiogram 3.x](https://docs.aiogram.dev/en/v3.22.0)
*   **База данных:** [SQLite](https://www.sqlite.org/docs.html) + [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20) (ORM) + [Alembic](https://alembic.sqlalchemy.org/en/latest) (миграции)
*   **Веб-парсинг:** [Requests](https://requests.readthedocs.io/en/latest) + [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest)
*   **Планировщик задач:** [APScheduler](https://apscheduler.readthedocs.io/en/stable/userguide.html)
*   **Безопасность:** [cryptography](https://cryptography.io/en/latest) (для шифрования учётных данных)

## 🚀 Установка и запуск

1.  **Клонирование репозитория:**
    ```bash
    git clone https://github.com/n1xsi/suai-deadline-bot.git
    cd suai-deadline-bot
    ```

2.  **Создание виртуального окружения:**
    *   На Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   На macOS / Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Установление зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройка переменных окружения:**
    *   Создайте файл `.env` в корневой папке проекта.
    *   Добавьте в него токен вашего telegram-бота и сгенерируйте ключ шифрования:

    ```.env
    BOT_TOKEN="Токен бота из @botfather"
    ENCRYPTION_KEY="Ключ, сгенерированный командой ниже"
    ```
    *   Для генерации `ENCRYPTION_KEY` выполните в терминале:
        ```bash
        python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
        ```

5.  **Запуск бота:**
    ```bash
    python -m src.bot.main_bot
    ```

## 📂 Архитектура проекта:
```
suai-deadline-bot/
├── .gitignore          # Настройки для игнорирования файлов в Git
├── LICENSE             # Лицензия проекта
├── README.md           # Файл, который вы сейчас читаете
├── requirements.txt    # Список всех библиотек, необходимых для работы проекта
│
└── src/                # Папка с основным исходным кодом
    │
    ├── bot/               # Компонент 1: всё, что связано с Telegram
    │   ├── __init__.py
    │   ├── filters.py     # Кастомные фильтры для хэндлеров
    │   ├── handlers.py    # Обработчики команд, FSM
    │   ├── keyboards.py   # Код для создания кнопок
    │   ├── main_bot.py    # Точка запуска бота
    │   └── states.py      # Класс состояний для FSM
    │
    ├── database/          # Компонент 2: База данных
    │   ├── __init__.py
    │   ├── engine.py      # Подключение к БД и создание сессий запросов
    │   ├── models.py      # Описание таблиц (User, Deadline)
    │   └── queries.py     # Функции для работы с БД
    │
    ├── parser/            # Компонент 3: Парсер
    │   ├── __init__.py
    │   └── scraper.py     # Функция для парсинга сайта ЛК
    │
    ├── scheduler/         # Компонент 4: Планировщик
    │   ├── __init__.py
    │   └── tasks.py       # Задачи для запуска по расписанию
    │
    ├── utils/             # Компонент 5: Утилиты
    │   ├── __init__.py
    │   └──crypto.py       # Функции для шифрования и дешифрования
    │
    └── config.py          # Файл для хранения настроек (токен бота, данные для БД)
```

Special thanks: [@f0rgenet](https://github.com/f0rgenet) - most important back-end help🙏
