num = input('Введите список чисел: ').split(' ')
i = [int(i) for i in num]
l = 1

if max(i) < 0:
    l += 0
    print(l)
else:
    while True:
        if l in i:
            l += 1
        elif l not in i:
            print(l)
            break