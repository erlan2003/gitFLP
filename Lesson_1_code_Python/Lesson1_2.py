def GetNameProject():
    name = ' Общество в начале 21 века'
    return name

print('Операции :\n',
      ' 1 - Вывод название проекта \n',
      ' 2 - Ввод возраста\n')
x = int(input(' Введите операцию : '))
if x == 1 :
    name = GetNameProject()
    print(' Название проекта : ', name)
    
elif x == 2 :
    age = int(input(' Введите свой возраст : '))
    if age >= 0 and age <= 7:
        print('\n Вам в детский сад !!!')
    elif age >= 7 and age <= 18:
        print('\n Вам в школу !!!')
    elif age >= 18 and age <= 25:
        print('\n Вам в профессиональное учебное заведение !!!')
    elif age >= 25 and age <= 60:
        print('\n Вам на работу !!!')
    elif age >= 60 and age <= 120:
        print('\n Вам на работу !!!')
    else:
        print('\n Это программа для людей !!!')
else:
    print(' Такой операции нет !!!')
    
    
