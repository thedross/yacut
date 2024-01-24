# YaCut

## Сервис YaCut - это одностраничный сервис укорачивания ссылок, а так же API для него.

Автор: [Федор Абаза](https://github.com/thedross)


### Стек использованных технологий:

- Python
- Flask
- SQLAlchemy

#### Развертывание проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env с переменными окружения:

- FLASK_APP = yacut
- FLASK_ENV = example: development
- DATABASE_URI = example: sqlite:///db.sqlite3
- SECRET_KEY = example: Secret

Запустить сервер командой:

```
flask run
```