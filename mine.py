#Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#Попросіть користувача ввести свсвій вік (можно використати константу або input()).
#- якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
#- якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#- якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
#- якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
#- у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача містить цифру тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні (неможливі) дані.

print("Wellcome to the cinema")
while True :
    user_input = input("Enter you`s age ")
    if user_input.isdigit():
        years = int(user_input) #Решил поменять переменную что бы избежать ошибок. Может и довольно трудновато но работает
        if years > 100 :
            print("Error. Try again")
        elif years < 0 :
            print("Error. Try again")
        elif years < 6 :
            print("Where are your parents?")
        elif years == 7 :
            print("You will be lucky!")
        elif years < 16 :
            print("This is a movie for adults!")
        elif years > 65:
            print("Show your pension certificate!")
        elif years :
            print("And there are no more tickets!")
    else: print("Error. Write your age") #Ещё раз с днём рождения, желаю счастья и здоровья

#Що ви бачите як результат цього курсу
#Хочу щоб найдалі мені було легчішу на шншоиу курсі

#Як ви збираєтесь використовувати цей результат
#Далі працювати з ним

#Чим ви готорі пожертвувати заради результату
#Час та сили