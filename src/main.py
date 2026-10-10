from src import processing, widget


test_list_widget = [
    'Maestro 1596837868705199',
    'Счет 64686473678894779589',
    'MasterCard 7158300734726758',
    'Счет 35383033474447895560',
    'Visa Classic 6831982476737658',
    'Visa Platinum 8990922113665229',
    'Visa Gold 5999414228426353',
    'Счет 73654108430135874305',
]

test_list_processing = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]


def widget_test() -> None:
    ''' Тест widget.py '''
    print('Test widget.py')
    for account_card_input in test_list_widget:
        print(f'if input = {account_card_input}; mask_account_card -> {widget.mask_account_card(account_card_input)}')
    print(f"widget.get_date('2024-03-11T02:26:18.671407') => {widget.get_date('2024-03-11T02:26:18.671407')}")


def processing_test() -> None:
    ''' Тест processing.py '''
    heading = 'filter_by_state(input_list_dict'
    print('Test processing.py')
    print(f'{heading}) -> {processing.filter_by_state(test_list_processing)}')
    print(f'{heading}, "CANCELED") -> {processing.filter_by_state(test_list_processing, 'CANCELED')}')
    print(f'{heading}, "") -> {processing.filter_by_state(test_list_processing, '')}')
    print(f'sort_by_date(input_list_dict) -> {processing.sort_by_date(test_list_processing)}')
    print(f'sort_by_date(input_list_dict, False) -> {processing.sort_by_date(test_list_processing, False)}')


widget_test()
processing_test()
