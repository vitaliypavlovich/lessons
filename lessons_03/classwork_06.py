'''
Взять список из предыдущей задачи, извлечь элементы со 2-го по 4-й включительно и вывести их в обратном порядке.
'''

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]

my_list = my_list[1:4]

print(my_list[::-1])