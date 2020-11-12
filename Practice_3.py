def my_func(arg_1, arg_2, arg_3):

    # Функция получает 3 аргумента (arg_1, arg_2, arg_3),
    # переводит их в список, и находит 2 макисмальных числа.
    # Возвращает сумму максимальных чисел

    l_args = [arg_1, arg_2, arg_3]
    l_args.remove(min(l_args))
    return sum(l_args)


print(my_func(1, 10, 3))
