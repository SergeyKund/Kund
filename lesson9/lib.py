import time
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


def time_decor(func):
    def sct(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        ex_time = end_time - start_time
        print(f'Виконано за {ex_time}')
        return result
    return sct()

