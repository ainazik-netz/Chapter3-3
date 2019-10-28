numbers = (input('Введите элементы списка через пробел: ')).split(' ')
step = int(input('Введите шаг: '))
def caesar (list_,steps):
    if steps > 0:
        for i in range(steps):
            list_.append(list_.pop(0))
    elif steps < 0: 
        steps = abs(steps)
        for i in range(steps):
                list_.insert(0,list_pop())
caesar(numbers,step)
print(numbers)
