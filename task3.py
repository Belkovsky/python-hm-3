#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

listnum = [1.11, 2.22, 3.33, 4.44, 5.55, 6]
print(f'Входной список: {listnum}')

newlist = []
for i in range(len(listnum)):
        if listnum[i]%1 != 0:                       # чтобы убрать числа без дробной части
            newlist.append(round(listnum[i]%1, 2))  # %1 - отделение от числа дробной части

answer = round(max(newlist) - min(newlist), 2)

print(f'Разница между max и min значениями дробной части: {answer}')   