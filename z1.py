#Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

n = int(input("input N: "))
if n > 0:
    text = ''
    for x in range(n):
        text += str(F(x+1)) + ' '
    file = open('fib.txt', 'w+')
    file.write(text)
    print('file created')

