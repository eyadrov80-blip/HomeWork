import pytest

from src.widget import mask_account_card, validate_account_card, get_date


@pytest.mark.parametrize(   'in_string,                     out_string',
                         [( 'Счёт 73654108430135874305',    'Счёт **4305'),
                          ( 'Счет 73654108430135874305',    'Счёт **4305'),
                          ( 'Счет73654108430135874305',     'Ошибка ввода данных'),
                          ( 'Счет 430135874305',            'Ошибка ввода данных'),
                          ( 'Счет 430135874305430135874305','Ошибка ввода данных'),
                          ( 'Maestro 1596837868705199',     'Maestro 1596 83** **** 5199'),
                          ( 'Visa Classic 6831982476737658','Visa 6831 98** **** 7658'),
                          ( 'МИР 8990922113665229',         'МИР 8990 92** **** 5229'),
                          ( 'Maestro 837868705199',         'Ошибка ввода данных'),
                          ( 'VisaClassic 6831982476737658', 'Ошибка ввода данных'),
                          ( 'МИР 89909221136652295656165',  'Ошибка ввода данных'),
                          ( '',                             'Ошибка ввода данных')])
def test_mask_account_card(in_string, out_string):
    assert mask_account_card(in_string) == out_string


@pytest.mark.parametrize(   'in_string,                     out_bool',
                         [( 'Maestro 1596837868705199',     True),
                          ( 'Счет 73654108430135874305',    True),
                          ( 'Mae stro1596837868705199',     True),
                          ( 'Счёт73654108430135874305',     True),
                          ( '',                             False)])
def test_validate_account_card(in_string, out_bool):
    assert validate_account_card(in_string) == out_bool


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    with pytest.raises(TypeError):
        get_date(123454689.123456)
    with pytest.raises(ValueError):
        get_date('')
    with pytest.raises(ValueError):
        get_date('jgvbnlkjsndvkhzbn')
