x = int(input(' Введите число от 1 до 9 : '))
if x >= 1 and x <= 3:
    s = input(' Введите строку : ')
    n = int(input(' Введите число повторов строки : '))
    for i in range(n):
        print(s)
elif x >= 4 and x <= 6:
    m = int(input(' Введите степень в которую следует возвести число : '))
    print(' Число',x,' в степени',m,' : ', x ** m)
elif x >= 7 and x <= 9:
    for i in range(10):
        x = x + 1
        print(x,'\n')
else:
    print('Ошибка ввода!!!')
