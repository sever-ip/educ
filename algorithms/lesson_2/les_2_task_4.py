'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('Введите кол-во n элементов для следующего ряда чисел: 1, -0.5, 0.25, -0.125 > '))

e = 1
s = 0

for i in range(n):
    s += e
    e /= -2

print('Сумма введенного кол-ва n элементов:', s)