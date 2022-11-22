# Простой телеграм бот [ru]

Небольшой фриланс проект бота для передачи пользователям инструкций по товарам.
Реализованные обработчики:
- Передача инстуркций и текста по 3-м товарам
- Загрузка и автоматическое добавление в репозиторий бота файлов (Доступно только для администартора бота)
- Фильтрация случайного текста (не связанные с командами для бота)


Проект развернут на VPS сервере.

Вы можете посмотреть на него по этой ссылке: https://t.me/Uspoilt_Bot

___________________________________________________

## Локальное развёртывание

Скопируйте через terminal репозиторий:
```bash
git clone https://github.com/FeltsAzn/Simple-tg-bot
```

#### Если вы работаете через редакторы кода `vim`, `nano`, `notepad` и другие:
Установка виртуального окружения, если у вас нет его локально.
```bash
python3 -m pip install --user virtualenv
```

Создайте виртуальное окружение в скопированном репозитории:
```bash
python3 -m venv env
```

Активируйте виртуальное окружение:
```bash
source env/bin/activate
```

Установите файл с зависимостями в виртуальном окружении:
```bash
(venv):~<путь до проекта>$ pip install -r requirements.txt
```

Создайте в папке `bot` файл `.env`
```bash
touch bot/.env
```

#### Если вы работаете через IDE:
Создайте файл ***.env*** в папке проекта ***bot***


Содержание файла `.env`
```sh
BOT_TOKEN = <Токен бота от BotFather>
ADMIN_ID = <telegram ID пользователя, кто будет отправлять файлы>
ADMIN_NAME = <Имя пользователя отвечающего за поддержку>
```

#### Docker контейнер
Вы можете развернуть приложение на сервере или локально в контейнере используя ***dockerfile***:
```bash
docker build . -t <название образа>
```

И запустить собранный образ в контейнере:
```bash
docker run -d <название образа>
```


________________________________________________________________

# Simple telegram bot [en]


A small freelance bot project to send product instructions to users.
Implemented handlers:
- Transfer of instructions and text for 3 products
- Downloading and automatically adding files to the bot repository (Available only for the bot admin starter)
- Random text filtering (not related to bot commands)


The project is deployed on a VPS server.

You can look at it from this link: https://t.me/Uspoilt_Bot

_____________________________________________________________

## Local deployment

Copy via terminal repository:
```bash
git clone https://github.com/FeltsAzn/Simple-tg-bot
```

#### If you are working with code editors `vim`, `nano`, `notepad` and others:
Installing a virtual environment if you don't have one locally.
```bash
python3 -m pip install --user virtualenv
```

Create a virtual environment in the copied repository:
```bash
python3 -m venv env
```

Activate the virtual environment:
```bash
source env/bin/activate
```

Install the dependency file in the virtual environment:
```bash
(venv):~<project path>$ pip install -r requirements.txt
```

Create a `.env` file in the `bot` folder
```bash
touch bot/.env
```

#### If you are using the IDE:
Create a ***.env*** file in the ***bot*** project folder


Contents of the `.env` file
```sh
BOT_TOKEN = <Bot Token from BotFather>
ADMIN_ID = <telegram ID of the user who will send files>
ADMIN_NAME = <Support username>
```

#### Docker container
You can deploy the application on a server or locally in a container using ***dockerfile***:
```bash
docker build . -t <image name>
```

And run the built image in a container:
```bash
docker run -d <image name>
```
