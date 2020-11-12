def int_func(str):

# Функция возвращает строку изменяя первую букву на большую

    return str.capitalize()


str = 'text surprise mother fucker'
title_str = [int_func(item) for item in str.split()]
print(' '.join(title_str))