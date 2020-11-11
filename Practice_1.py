def segmentation (arg_1, arg_2):

# 'Функция для деления чисел arg_1, arg_2\n'
# 'Возвращается число, при "0" выпадает сообщение о запрете делить на "0"

    if arg_2 == 0:
        print(f'У вас не получиться разделить {arg_1} на {arg_2}')
        pass
    else:
        return arg_1 / arg_2


arg_1 = float(input('Введите делимое число: '))
arg_2 = float(input('Введите делитель: '))

print(f'Результат: {segmentation(arg_1, arg_2)}')