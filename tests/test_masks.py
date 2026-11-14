import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('1234546890123456') == '1234 54** **** 3456'
    assert get_mask_card_number('') == ' ** **** '
    assert get_mask_card_number('123454689012') == '1234 54** **** 9012'
    assert get_mask_card_number('12345468901234567890') == '1234 54** **** 7890'
    assert get_mask_card_number('qwerqwerqwerqwer') == 'qwer qw** **** qwer'

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(1234546890123456)


def test_get_mask_account():
    assert get_mask_account('12345678901234567890') == '**7890'
    assert get_mask_account('') == '**'
    assert get_mask_account('1234567890') == '**7890'
    assert get_mask_account('123456789012345678901234') == '**1234'
    assert get_mask_account('1234567890qwertyuiop') == '**uiop'

    with pytest.raises(TypeError) as exc_info:
        get_mask_account(123454689.123456)