'''
В школе решили набрать три новых класса по программированию.
Так как занятия у них проходят в одно и то же время, было решено выделить кабинет для каждого класса
и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
'''
from functools import reduce

def desks(*args):
    total = 0
    for i in args:
        number_of_desks = i // 2
        total += number_of_desks
        if i % 2 == 1:
            total += 1
    print(total)


desks(13, 13, 13)