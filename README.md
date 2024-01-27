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
git clone https://github.com/thedross/yacut
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

Создать БД по на основе migrations/:

```
flask db upgrade
```
запустите сервер командой:
```
flask run
```


## Справка по использованию:

#### Одна главная страница с формой из двух полей:
  1. Длинная исходная ссылка. Обязательна для заполнения.
  2. Пользовательский вариант короткой ссылки (менее 16 символов). Необязательна для заполнения.

Если пользователь предложит вариант короткой ссылки, который уже занят, то сервис сообщает пользователю об этом уведомлением.
Если пользователь не введет короткий вариант, он будет сгенерирован автоматически.
Для короткой ссылки можно использовать:
  - большие латинские буквы,
  - маленькие латинские буквы,
  - цифры в диапазоне от 0 до 9.

В случае успеха после отправки формы на главной странице отображается созданная ссылка.

#### Взаимодействие через API:
  1.
  /api/id/ — POST-запрос на создание новой короткой ссылки;
  2.
  /api/id/<имя_короткой_ссылки>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.