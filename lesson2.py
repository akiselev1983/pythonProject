# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add, all_todo = notebook()
add('hi')
add('hello')
add('world')
print(all_todo())

####################################################################################################################
# 2) протипізувати перше завдання
from typing import Callable


#def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]] ]:
def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add_nb1, all_todo_nb1 = notebook()
add_nb2, all_todo_nb2 = notebook()
add_nb1('privet')
add_nb1('poka')
add_nb2('good')
add_nb2('byi')
print(all_todo_nb1())
print(all_todo_nb2())
#####################################################################################################################
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
str1 = ''


def expanded_form(num: int):
    l = []
    j = len(str(num))
    for i in str(num):
        j -= 1
        if i != '0':
            l.append(i + ('0' * j))
    print(' + '.join(l))


def expanded_form1(n: int):
    st = str(n)
    length = len(st) - 1
    sum = []
    for i, ch in enumerate(st):
        if ch != '0':
            sum.append(ch + '0' * (length - i))
    print(' + '.join(sum))
    print(length)


def expanded_form2(n: int):
    st = str(n)
    length = len(st) - 1
    print(' + '.join(ch + '0' * (length - i) for i, ch in enumerate(st) if ch != '0'))


def expanded_form3(n: int):
    return ' + '.join([ch + '0' * (len(str(n)) - 1 - i) for i, ch in enumerate(str(n)) if ch != '0'])


expanded_form(70002)
expanded_form1(70002)
expanded_form2(70002)
print(expanded_form3(70002))


#####################################################################################################################

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій
def decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('count: ', count)
        func(*args, **kwargs)
        print('--------------')

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func1()

#####################################################################################################################
