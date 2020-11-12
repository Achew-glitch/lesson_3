def check_spec_symbol (arg):
    if arg[len(arg)-1] == '#':
        arg = arg[:len(arg) - 1]
        summator(arg)
        return False
    else:
        return True


def summator(arg):
    global current_sum
    sum_el = [int(item) for item in arg.split()]
    current_sum += sum(sum_el)
    print(current_sum)


global current_sum
current_sum = 0

while True:
    l_num = input('Введите строку чисел: ')
    if check_spec_symbol(l_num):
        summator(l_num)
    else:
        break
