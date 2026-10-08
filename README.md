@'
# HomeWork_9_1

Домашняя работа "9.1 Poetry. Оформление кода"

Модуль main.py совершает вызов функций из модуля masks.py с передачей различных аргументов.  

Модуль masks.py содержит две функции:


get_mask_card_number(pan_input: object) -> str

    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX,
    где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры,
    разделенным пробелами.
    Пример работы функции при валидном вводе:
    входной аргумент = '7000792289606361'
    возвращает = '7000 79** **** 6361'
    Примечание:
    pan_input - PAN = Primary Account Number (номер карты)

get_mask_account(pan_input: object) -> str

    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    Пример работы функции при валидном вводе:
    входной аргумент = '73654108430135874305'
    возвращает = '**4305'
    
validate_and_normalize_pan(pan_input: object) -> Tuple[bool, str]

    Проверяет, что входной аргумент содержит ровно 16 цифр.
    Разрешены только цифры, пробелы и тире.
    Возвращает:
        (True, "1234567890123456") — если валидно и нормализовано.
        (False, "") — если невалидно.


## Статус
В разработке.

## Зависимости
Установлены НЕ через Poetry.

СЛОЖНОСТИ:

1. DNS работает, соединение открывается, но ответа от сервера нет — «Read timed out». Это значит, что пакеты не доходят до тебя с CDN PyPI (он работает на Fastly, и из российских сетей соединения с ним часто обрываются по таймауту — это известная ситуация, а не проблема твоего Poetry). В июне такое уже случалось: PyPI временно «отваливался», потом доступ восстанавливался, но стабильность зависит от провайдера. 
skillbox.ru +1

РЕШЕНИЕ: Переключиться на зеркало пакетов. Добавь зеркало как основной источник — Poetry сам пропишет его в pyproject.toml: >_ poetry source add --priority=primary mirror https://mirror.yandex.ru/pypi/simple/

Если зеркало Яндекса тупит (его иногда ругают за медленную синхронизацию), попробуй вместо него:
https://pypi-mirror.gitverse.ru/simple/
или китайские (они обычно быстрые, но чуть отстают по свежим версиям):
https://pypi.tuna.tsinghua.edu.cn/simple
https://mirrors.aliyun.com/pypi/simple

Чтобы убрать зеркало и вернуться на PyPI: >_ poetry source remove mirror

FLAKE8 поставил через POETRY с зеркала

2. MYPY, BLACK и ISORT встали только через PIP
>pip install --retries 20 --timeout 120 mypy -i https://pypi-mirror.gitverse.ru/simple/

>poetry add --group lint mypy

>pip install --retries 20 --timeout 120 black -i https://pypi-mirror.gitverse.ru/simple/

>poetry add --group lint black 

> pip install --retries 20 --timeout 120 isort -i https://pypi-mirror.gitverse.ru/simple/

> poetry add --group lint isort

## Как запустить
```bashn
poetry install --no-root
poetry run homework

poetry run python -m src.main