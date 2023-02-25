#1. Напишіть функцію, яка б приймала номер місяця, а вертала його назву.
def monthes(month):
    list_of_month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    try:
        return list_of_month[month]
    except KeyError:
         return 'KeyError: try again and print number from 1 to 12'

try:
    month_name = monthes(int(input('Input number of month: ')))
    print(month_name)
except ValueError as error2:
    print('ValueError: try again and print number from 1 to 12')

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
class Game:
    class GameRates(Exception):
        def __init__(self, rate):
            self.rate = rate

        def __str__(self):
            return f"Invalid game rate: {self.rate}. Game rate should be between 1 and 10."

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

        if not 1 <= rate <= 10:
            raise Game.GameRates(rate)

    def __str__(self):
        return f"Game: {self.name}, Rate: {self.rate}"

# Приклад використання
try:
    new_game = Game(input("Input game name: "), int(input("Input game rate: ")))
    print(new_game)
except ValueError as error:
    print(f"{error}: please input rate as integer from 1 to 10.")
except Game.GameRates as error:
    print(error)
