#1. Напишіть функцію, яка б приймала номер місяця, а вертала його назву.
def monthes(month):
    list_month = ['Winter','Spring', 'Summer','Autumn']
    if month in (1, 2, 12):
        try:
            return Winter
        except NameError as error:
            print(f'ERROR: {error}')
        finally:
            return 'Winter'
    elif month in (3, 4, 5):
        return 'Spring'
    elif month in (6, 7, 8):
        return 'Summer'
    elif month in (9, 10, 11):
        try:
            return list_month[4]
        except IndexError as error3:
            print(f'ERROR3: {error3}')
        finally:
            return 'Autumn'

try:
    print(monthes(int(input('Click here to input a number of month to know a time of the year: '))))
except ValueError as error2:
    print(f'ERROR2: {error2}')
    print('Please try again and print integer')

#2. Напишіть програму яка б приймала список з числами та перевіряла чи всі числа в ньому унікальні. Реалізуйте з виключаннями.
def program(list_of_strings):

    decision = (input(f'Ви хочете використовувати для обробки список: {comp_list}, чи хочите додати елемент?(так/ні): '))
    if decision == 'ні':
        pass
    elif decision == 'так':
        one_more_element = (input('Введіть додаткове число: '))
        try:
            list_of_strings.append(int(one_more_element))
        except ValueError as error3:
            print(f'{error3}')
            pass
    unique_list = ()
    for i in list_of_strings:
        if list_of_strings.count(i) == 1:
            try:
                unique_list.append(i)
            except AttributeError as error:
                print(f'{error}')
                unique_list = []
                unique_list.append(i)
    print('Унікальний список:',end=' ')
    print(unique_list)

    iteration_list = [int (i) for i in list_of_strings if list_of_strings.count(i) > 1]
    print('Значення, які повторюються:',end=' ')
    print(iteration_list)

comp_list = [1.0, 2, 1, 10, 10, 23, 11, 0, 17, 10, 120, 0, 17, 123]
program(comp_list)


#3. Напишіть користувацький клас виключення з функціоналом на свій вибір. Викличте його за допомогою raise.
class GameRates(Exception):
    def __init__(self, rate, minrate, maxrate):
        self.rate = rate
        self.minrate = minrate
        self.maxrate = maxrate

    def __str__(self):
        return f'Unacceptable rate {self.rate} for game. \
Rate should be from {self.minrate} to {self.maxrate}'

class Game:
    def __init__(self, name, rate):
        self.name = name
        minrate = 1
        maxrate = 10
        if minrate < rate < maxrate:
            self.rate = rate
        else:
            raise GameRates(rate, minrate, maxrate)

    def display(self):
        print(f'Game: {self.name}, rate: {self.rate} ')


new_game = Game(input('Input game '), int(input('Input rate ')))
new_game.display()
