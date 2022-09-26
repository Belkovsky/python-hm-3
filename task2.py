#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import RandomNum as r
list = r.newlist()

print(f'Сгенерированный список: {list}')

list2 = []
count = 1
for i in range(len(list) // 2):
    n = list[i] * list[i-count]
    count += 2
    list2.append(n)
if len(list) % 2 == 1: 
    list2.append(list[int(len(list) / 2)] ** 2)

print(list2)
