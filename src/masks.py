from typing import Tuple


def get_mask_card_number(pan_input: object) -> str:
    '''
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
    '''
    is_valid_pan, normalized_pan = validate_and_normalize_pan(pan_input)
    if is_valid_pan:
        return normalized_pan[0:4] + ' ' + normalized_pan[4:6] + '** ****' + normalized_pan[-4:]
    else:
        return 'error_card_number'


def get_mask_account(pan_input: object) -> str:
    '''
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    Пример работы функции при валидном вводе:
    входной аргумент = '73654108430135874305'
    возвращает = '**4305'
    '''
    is_valid_pan, normalized_pan = validate_and_normalize_pan(pan_input, False)
    if is_valid_pan:
        return '**' + normalized_pan[-4:]
    else:
        return 'error_card_number'


def validate_and_normalize_pan(pan_input: object, check_length_pan: bool = True) -> Tuple[bool, str]:
    """
    Если второй аргумент TRUE или не указан проверяет, что входной аргумент содержит ровно 16 цифр.
    Разрешены только цифры, пробелы и тире.
    Возвращает:
        (True, "1234567890123456") — если валидно и нормализовано.
        (False, "") — если невалидно.
    """
    # Проверим что pan_input является строкой
    if not isinstance(pan_input, str):
        return False, ""
    # Оставляем только цифры, пробелы и тире; остальные символы делают ввод невалидным
    # Создадим "Белый список" в виде множества
    allowed_chars = set("0123456789 -")
    # Пробежимся по pan_input и сравним с "Белым списком"
    if any(ch not in allowed_chars for ch in pan_input):
        return False, ""
    # Создадим новую строку без разделителей
    digits_only = pan_input.replace(" ", "").replace("-", "")
    # Проверим количество символов в итоговой строке
    if len(digits_only) != 16 and check_length_pan:
        return False, ""
    elif len(digits_only) < 4:
        return False, ""

    # Проверим что строка состоит из цифр
    if not digits_only.isdigit():
        return False, ""
    # Все проверки пройдены, возвращаем TRUE и "Чистые" данные
    return True, digits_only
