from src import masks


def masks_test() -> None:
    print('Test masks')
    pan_input = '1234567890123456'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '1234 5678 9012 3456'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '12 34 56 78 90 12 34 56'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '1234-5678-9012-3456'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '12-34-56-78-90-12-34-56'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '1234 5678-9012- 3456'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '12 34-56  78--90 -12- - 34               -------------- 56'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '123456789012345'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '12345678901234567'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '1234 5678-9012 - 345'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '12-34 56--78  90---12   34----56    7'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = 'x123456789012345'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = 'abcdabcdabcdabcd'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input_int = 1234567890123456
    print(f'if input int = {pan_input_int}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input_int)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input_int)}')

    pan_input_float = 12345678.90123456
    print(f'if input float = {pan_input_float}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input_float)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input_float)}')

    pan_input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    print(f'if input = {pan_input_list}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input_list)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input_list)}')

    pan_input_dict = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
    print(f'if input = {pan_input_dict}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input_dict)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input_dict)}')

    pan_input = '7000792289606361'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '73654108430135874305'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '361'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '----    ----    4305'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = ''
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')

    pan_input = '--- 4 3 5'
    print(f'if input = {pan_input}')
    print(f'get_mask_card_number -> {masks.get_mask_card_number(pan_input)}')
    print(f'get_mask_account -> {masks.get_mask_account(pan_input)}')


masks_test()
