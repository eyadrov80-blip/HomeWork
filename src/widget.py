import re
from typing import List, Tuple
from datetime import datetime

from src import masks


# Компилируем один раз — удобно и чуть быстрее при частых вызовах
# «Счет/Счёт» + хотя бы один пробел
ACCOUNT_PATTERN = re.compile(r"Сч[её]т\s+(\d{20})", re.IGNORECASE)
# Каждой системе — свой шаблон, читается и расширяется легко
CARD_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("Visa", re.compile(r"Visa(?:\s+\w+)*\s+(\d{16})", re.IGNORECASE)),
    ("MasterCard", re.compile(r"Master\s?Card\s+(\d{16})", re.IGNORECASE)),
    ("Maestro", re.compile(r"Maestro\s+(\d{13,19})", re.IGNORECASE)),
    ("МИР", re.compile(r"МИР\s+(\d{16})", re.IGNORECASE)),
    ("American Express", re.compile(r"(?:American\s+Express|AmEx)\s+(\d{15})", re.IGNORECASE)),
    ("JCB", re.compile(r"JCB\s+(\d{16})", re.IGNORECASE)),
    ("UnionPay", re.compile(r"Union\s?Pay\s+(\d{16,19})", re.IGNORECASE)),
    ("Discover", re.compile(r"Discover\s+(\d{16})", re.IGNORECASE)),
    ("Diners Club", re.compile(r"Diners\s+Club\s+(\d{14})", re.IGNORECASE)),
]


def mask_account_card(account_card: str) -> str:
    '''
    Функция принимает строку, содержащую тип и номер карты или счета.
    Аргументом может быть строка типа Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или Счет 73654108430135874305.
    Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!
    Возвращать строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки.
    '''
    if not validate_account_card(account_card):
        return 'Ошибка ввода данных'
    match = ACCOUNT_PATTERN.fullmatch(account_card.strip())
    if match:
        if len(match.group(1)) >= 4:
            return f"Счет {masks.get_mask_account(match.group(1))}"
        else:
            return 'Ошибка ввода данных'

    line = account_card.strip()
    for name, pattern in CARD_PATTERNS:
        match = pattern.fullmatch(line)
        if match:
            return f"{name} {masks.get_mask_card_number(match.group(1))}"
    return 'Данные не распознаны'


def validate_account_card(account_card: str) -> bool:
    """
    Функция валидности.
    Проверяет: На входе строка, строка не пустая.
    Возвращает: True — если валидно и False — если невалидно.
    """
    #   if not isinstance(account_card, str):   # Проверим что account_card является строкой
    #       return False
    if not account_card:  # Проверим что account_card не пустая строка
        return False
    return True


def get_date(iso_string: str) -> str:
    '''
    :param iso_string: "ГГГГ-ММ-ДД Т ЧЧ:ММ:СС.СССССС" (Пример: "2024-03-11T02:26:18.671407")
    :return:    "ДД.ММ.ГГГГ" (Пример: "11.03.2024")
    '''
    return datetime.fromisoformat(iso_string).strftime("%d.%m.%Y")

