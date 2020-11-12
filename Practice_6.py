def int_func(str):
    return str.capitalize()


str = 'text surprise mother fucker'
title_str = [int_func(item) for item in str.split()]
print(' '.join(title_str))