'''
Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
'''

n = int(input('Введите n'))
for i in range(0, 101):
    if i % n == 0:
      print(i)


