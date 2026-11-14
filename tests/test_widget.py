import pytest

from src.widget import mask_account_card, validate_account_card, get_date


def test_mask_account_card():
    pass


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
