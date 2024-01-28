# Требуется найти все телефонные номера в заданном тексте.
def is_phone_number(phone):
    groups = phone.split('-')
    if len(groups) != 3:
        return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars)


def get_all_num(text):
    for c in range(len(text)):
        chunk = text[c:c + 12]
        if is_phone_number(chunk):
            yield chunk


txt = ('Привет всем, мой номер 919-654-8765, а еще у меня есть два дополнительных номера:543-780-0898 и 123-765-8907. '
       'Вот и все!')

print(list(get_all_num(txt)), end=' ')
