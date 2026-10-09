from datetime import datetime
from typing import Any, Dict, List


# fmt: off
def filter_by_state(input_list_dict: List[Dict[str, Any]],
                    state: str = "EXECUTED"
                    ) -> List[Dict[str, Any]]:
    '''
    Возвращает новый список словарей, отфильтрованный по значению ключа 'state'.
    :param input_list_dict: список словарей с данными
    :param state: значение для фильтрации по ключу 'state'; по умолчанию 'EXECUTED'
    :return: новый список отфильтрованных словарей
    '''
# fmt: on
    return [input_list_dict for input_list_dict in input_list_dict if input_list_dict.get("state") == state]


# fmt: off
def sort_by_date(input_list_dict: List[Dict[str, Any]],
                 sort_order: bool = True
                 ) -> List[Dict[str, Any]]:
    '''
    Сортирует список словарей по полю 'date'.
    :param input_list_dict: Список словарей, в каждом ожидается ключ 'date', ISO-строкой.
    :param sort_order: Если True — сортировка по убыванию (от новых к старым),
                       если False — по возрастанию. По умолчанию True.
    :return: Новый отсортированный список.
    '''
# fmt: on
    return sorted(input_list_dict, key=lambda item: datetime.fromisoformat(item["date"]), reverse=sort_order)
