#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Negafibonacci(fib):
    
    if fib < 0: fib *= -1

    a = b = 1
    listfib1 = [1, 1]

    for i in range(2, fib):
        a, b = b, b + a
        listfib1.append(b)
    
    a = b = 1                     # возвращаем значение а и b к изначальному
    for j in range(-fib, 1):
        a, b = b, a - b
        listfib1.insert(0, b)
    
    return(listfib1)

num = int(input('Введите число для составления ряда Фибоначчи: '))

list = ((Negafibonacci(num)))

print(list)
