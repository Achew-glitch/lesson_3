def profile (f_name, l_name, age, town, email, number):
    return f'{f_name}, {l_name}, {age}, {town}, {email}, {number}'

print(
    profile(f_name=input('Введите имя: '),
        l_name=input('Введите фамилию: '),
        age=input('Введите дату рождения: '),
        town=input('Введите город проживания: '),
        email=input('Введите адрес электронной почты: '),
        number=input('Введите свой номер телефона: ')))