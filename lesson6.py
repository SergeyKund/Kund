# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.
# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів
# Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад :


def input_float(value) :
     try:
         res = float(value)
         print(res)
     except ValueError:
         res = print(0)
     return res
res = input_float(value=input("Enter "))


def int_float_str(value_1, value_2) :
    if isinstance(value_1, (int,float)) and isinstance(value_2, (int,float)):
        print(value_1 * value_2)
    elif isinstance(value_1, (str)) and isinstance(value_2, (str)):
        print(value_1 + value_2)
    else:
        print(value_1, value_2)
user_input_1 = input('Enter 1 ')
user_input_2 = input('Enter 2 ')
try:
    value_1 = float(user_input_1)
except:
    value_1 = user_input_1

try:
    value_2 = float(user_input_2)
except:
    value_2 = user_input_2
int_float_str(value_1, value_2)




def years_input(year_number):
    arg_2 = year_number % 10
    if 5 <= year_number <= 20:
        res = f'{year_number} років'
    elif arg_2 == 1:
        res = f'{year_number} рік'
    elif 2 <= arg_2 <= 4:
        res = f'{year_number} роки'
    elif 5 <= arg_2 <= 9:
        res = f'{year_number} років'
    else:
        res = f'{year_number} років'
    return res

def wellcome():
    print("Ласкаво просимо до кінотеатру")

def user_input():
    while True:
        input_1 = input("Напишіть свій вік: ")
        if input_1.isdigit():
            input_1 = int(input_1)
            examination_wrorg(exam=input_1)
        else:
            print('Помилка. Введіть ваш вік')

def examination_wrorg(exam):
    if exam > 100:
        print("Помилка. Спробуйте знову")
    elif exam <= 0:
        print("Помилка. Спробуйте знову")
    else:
        examination_correct(correct=exam)

def examination_correct(correct):
    res = years_input(year_number=correct)
    if "7" in str(correct):
        print(f'Незважаючи на те, що вам {res}, квитків всеодно немає!')
    elif correct < 7 :
        print(f'Вам {res}, вам пощастить')
    elif correct < 16 :
        print(f"Тобі лише {res}, а це фільм для дорослих!")
    elif correct > 65:
        print(f"Вам {res} ? Покажіть пенсійний посвідчення!")
    elif correct:
        print(f'Незважаючи на те, що вам {res}, квитків всеодно немає!')

def cashier():
    wellcome()
    user_input()

cashier()