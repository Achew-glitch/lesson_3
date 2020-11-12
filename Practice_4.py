def my_func (arg_1, arg_2):
    res = arg_1
    for i in range(arg_2, 1):
        res /= arg_1
    return res

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print(my_func(x, y))
print(pow(x, y))
