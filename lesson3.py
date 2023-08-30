# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

# my_word = input("Enter word: ")
# my_number = int(input("Enter number: "))
# if 0 <= my_number <= len(my_word):
#     sym = my_word[my_number]
#     print(f"The {my_number} in {my_word} is {sym} ")
# else: print("Error")

# print("Hello")
# user_input = input("Enter your word :")
# res = len(user_input)
# print(res)

my_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 2.2, 'Python', 9, 0, 'Lorem Ipsum']
my_list2 =[]
for my_list3 in my_list:
    if type(my_list3) == int:
        my_list2.append(my_list3)
    elif type(my_list3) ==float:
        my_list2.append(my_list3)
print(my_list2)