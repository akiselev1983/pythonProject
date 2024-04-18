
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'
res = []
for i in st:
    if i.isnumeric():
        res.append(i)
    else:
        continue
res1 = ','.join(res)
print(res1)
print(','.join(res))
print(','.join([ch for ch in st if ch.isdigit()]))
#################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
str1 = 'as 23 fdfdg544 34'

res2 = []
st2 = ''
for i in str1:
    if i.isnumeric() or i == ' ':
        res2.append(i)

print(','.join(''.join(res2).split()))
print(','.join(''.join(ch if ch.isdigit() else ' ' for ch in str1).split()))
#################################################################################

#list comprehension

# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
print([i.upper() for i in greeting])
print(list(greeting.upper()))
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#####################################################################################
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([i**2 for i in range(50) if i % 2 == 1])
print([i**2 for i in range(50) if i % 2])
#####################################################################################
#function

#- створити функцію яка виводить ліст
l = [1,2,3,4,5]
def func(x):
    print(x)
func(l)
#- створити функцію яка приймає три числа та виводить та повертає найбільше.
def func1(a,b,c):
    max_num = max(a,b,c)
    print(max_num)
    return max_num
func1(2,5,9)
#- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def func2(*args):
    max_num = max(args)
    min_num = min(args)
    print(max_num)
    return min_num
func2(4,5,6,1,5,8)
#- створити функцію яка повертає найбільше число з ліста
def func3(list):
    max_num = max(list)
    print(max_num)
    return max_num
func3([6,7,8])
#- створити функцію яка повертає найменьше число з ліста
def func4(list):
    min_num = min(list)
    print(min_num)
    return min_num
func4([6,7,8])
#- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def func5(list):
    sum_num = sum(list)
    print(sum_num)
    return sum_num
func5([6,7,8])
#- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def func6(list):
    print(sum(list) / len(list))
    return sum(list) / len(list)
func6([5,6,7,8])




################################################################################################
# 1)Дан list:
list1 = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
def min_num():
    print(min(list1))

#print(min(list1))

#   - видалити усі дублікати
def del_dub():
    print(list(set(list1)))

# print(list(set(list1)))

#   - замінити кожне 4-те значення на 'X'
def to_x():
    print(['X' if (i + 1) % 4 == 0 else item for i, item in enumerate(list1)])

# print(['X' if i % 4 == 0 else list1[i] for i in range(len(list1))])

# print(['X' if (i+1) % 4 == 0 else item for i, item in enumerate(list1)])

# for i in list1:
#     if list1.index(i) % 4 == 0:
#         list1[list1.index(i)]='X'
# print(list1)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(a):
    for i in range(a):
        if i == 0 or i == (a-1):
            print('*'*a)
        else:
            print('*' + ' '*(a-2) + '*')

# square(7)

# 3) вывести табличку множення за допомогою цикла while
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(j*i, end='\t')
#         j += 1
#     print()
#     i += 1
# print()
def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            print(res, end='\t')
            j += 1
        i += 1
        print()



# 4) переробити це завдання під меню
while True:
    print('1) Знайти мін число:')
    print('2) Видалити дублікати:')
    print('3) Замінити кожне 4-те значення на X: ')
    print('4) Вивести квадрат:')
    print('5) Вивести табличку множення:')
    print('0) Вихід:')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        min_num()
    elif choice == '2':
        del_dub()
    elif choice == '3':
        to_x()
    elif choice == '4':
        square(5)
    elif choice == '5':
        multi_table()
    elif choice == '0':
        break


# So1dest, [16.04.2024 11:49]
# надіюсь не в азкабані)