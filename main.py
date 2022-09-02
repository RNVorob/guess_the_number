from random import *
print('Добро пожаловать в числовую угадайку.')

def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= x
          
def is_valid_cont():
    while True:
        n = input('введите "Да" или "Нет": ')
        if n.lower() not in ['да', 'нет', 'д', 'н']:
            print('Не понял? проверьте правильность ввода вашего решения')
            continue
        elif n.lower() == 'нет' or n.lower() == 'н':
            print('Спасибо, что играли в нашу угадайку. Пока.')
            break
        else:
            game()

def game():
    print('Напишите предельную границу интервала')
    global x
    x = int(input())
    print('Попробуйте отгадать целое число от 1 до', x, 'которое я загадал.')
    count = 0
    num = randint(1, x)
        while True:
        s = input('Введите свой вариант числа: ')
        if is_valid(s) == False:
            print('Будьте внимательней, введите именно целое число от 1 до', x, 'включительно.')
            continue
        else:
            if int(s) < num:
                print('Ваше число меньше загаданного числа, попробуйте снова: ')
            elif int(s) > num:
                print('Ваше число больше загаданного числа, попробуйте снова: ')
            elif int(s) == num:
                print('Точно! это то число, что я загадал. Поздравляю!')
                break
            count += 1
    if count in (2, 3, 4):
        print('Вы справились за', count, 'попытки. Хотите ещё сыграть?')
    elif count == 1:
        print('Вы справились за', count, 'попытку. Хотите ещё сыграть?')
    else:
        print('Вы справились за', count, 'попыток. Хотите ещё сыграть?')

game()       

is_valid_cont()
