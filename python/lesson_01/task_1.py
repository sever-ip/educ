'''
Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, 
выведите на экран.
'''
name = 'Name'
surname = 'Surname'
age = 30

print('Здравствуйте, %s %s! Вам %d?' %(name, surname, age))
print('Здравствуйте, {} {}! Вам {}?'.format(name, surname, age))
print(f'Здравствуйте, {name} {surname}! Вам {age/2:.2f}?')

country = input('В какой стране Вы проживаете? ')
city = input('В каком городе Вы проживаете? ')
year = int(input('Сколько лет Вы в нем проживаете? '))

print('{}, Вы проживаете в чудесной стране - {}! И уже целых {} лет в замечательном городе - {}. Поздравляем!'.format(name, country, year, city))
