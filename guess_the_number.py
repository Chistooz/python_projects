import random



def is_valid(n):                    #Проверка на соотвествие условию
    return 1 <= n <= 100


def comrare_num(up_num):                      #Сравнение введённого числа и загадонного
    num = random.randint(1, int(up_num))
    count = 0
    while True:
        user_number = input('Угадывай \n')
        count += 1
        user_number = int(user_number)
        if is_valid(user_number):
            if user_number > num:
                print('Ваше число больше загаданного \n')
            elif user_number < num:
                print('Ваше число меньше загадонного \n')
            else:
                print('Поздравляю, вы отгадали с', count, 'раза')
                break
        else:
            print('Какое то неправильное число ты ввёл, давай ещё раз попробуй')



def game():                                           #Игра
    print('Добро пожаловать в игру "Угадайка". \n')

    while True:
        continue_answer = input('Сыграем? (Д,д - сыграем, Н,н - завязывай)')
        if continue_answer == 'Н' or continue_answer == 'н':
            print('До скорого, заглядывай поиграть')
            break
        elif continue_answer == 'Д' or continue_answer == 'д':
            print('Укажите до какого числа мне загадывать (до 100 включительно)')
            x = input()
            print('Введите число от 1 до', x)
            comrare_num(x)
        else:
            print('Я не понял тебя, ответь ещё раз. \n')




game()


