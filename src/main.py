from src import widget


test_list = [
    'Maestro 1596837868705199',
    'Счет 64686473678894779589',
    'MasterCard 7158300734726758',
    'Счет 35383033474447895560',
    'Visa Classic 6831982476737658',
    'Visa Platinum 8990922113665229',
    'Visa Gold 5999414228426353',
    'Счет 73654108430135874305',
]


def widget_test() -> None:
    print('Test widget.py')
    for i in test_list:
        print(f'if input = {i}; mask_account_card -> {widget.mask_account_card(i)}')


widget_test()
