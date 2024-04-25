
# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

from typing import Self


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    def __add__(self, other: Self):
        return self.area + other.area
    def __sub__(self, other):
        return self.area - other.area
    def __eq__(self, other):
        return self.area == other.area
    def __ne__(self, other):
        return self.area != other.area
    def __gt__(self, other):
        return self.area > other.area
    def __lt__(self, other):
        return self.area < other.area
    def __len__(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(10, 20)
rect2 = Rectangle(5, 10)

print(Rectangle(5, 10).__add__(rect1))
print(rect1.__sub__(rect2))

####################################################################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        return cls.__count
class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
    def shoe_cinderella(self, l:list[Cinderella]):
        for i in l:
            if i.foot_size == self.shoe_size:
                return print(f'Prince-{self.name}:{self.shoe_size}=={i.name}-{i.foot_size} was cinderella')


l1: list[Cinderella] = [Cinderella('Karina', 18, 32),
                       Cinderella('Mila', 19, 36),
                       Cinderella('Anna', 20, 40),
                       Cinderella('Olia', 21, 44),
                       Cinderella('Luba', 20, 36)]
prince1 = Prince('Max', 28, 36)
prince2 = Prince('Bob', 66, 44)
prince1.shoe_cinderella(l1)
prince2.shoe_cinderella(l1)
print(Cinderella.get_count())
###################################################################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
#   класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod
class Printable(ABC):

    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'Book: {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'Magazine: {self.name}')

class Main:
    __printable_list: list[Printable] = []
    @classmethod
    def add(cls, item):
        if isinstance(item, Printable):
            cls.__printable_list.append(item)
    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.__printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()
    @classmethod
    def show_all_books(cls):
        for book in cls.__printable_list:
            if isinstance(book, Book):
                book.print()

m1 = Magazine('Major')
m2 = Magazine('Minor')
m3 = Magazine('House')
b1 = Book('Bob')
b2 = Book('Mila')
b3 = Book('Luba')
b4 = Book('Anna')

Main.add(m1)
Main.add(m2)
Main.add(m3)
Main.add(b1)
Main.add(b2)
Main.add(b3)
Main.add(b4)

Main.show_all_books()
Main.show_all_magazines()

# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()

# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False