from typing import Any, Dict, List, Optional


def filter_by_state(input_list_dict: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, отфильтрованный по значению ключа 'state'.

    Если state=None, возвращаются все записи (без фильтрации по этому ключу).
    Если ключ 'state' отсутствует в словаре, такая запись не попадёт в результат
    при фильтрации по конкретному состоянию.

    :param records: список словарей с данными
    :param state: значение для фильтрации по ключу 'state'; по умолчанию 'EXECUTED'
    :return: новый список отфильтрованных словарей
    """
    if state is None:
        # Если состояние не задано — возвращаем копию списка
        return list(input_list_dict)

    return [input_list_dict for input_list_dict in input_list_dict if input_list_dict.get("state") == state]


def sort_by_date(input_list_dict: List[Dict[str, Any]], sort_order: bool = True) -> List[Dict[str, Any]]:
    '''

    :return:
    '''
    return list(input_list_dict)
