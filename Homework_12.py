# Задание из видео "Python для начинающих 14"

# Подзадание №1: Сделать инт такой, что 2+2 = 5
# Это должно реализоваться с помощью перегрузкой операторов
class Pseudo_Int(int):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value + 1

# Подзадание №2: Сделать лист такой, что больше 10 элементов нельзя
class Pseudo_list(list):
    def __init__(self, values):
        if len(values) > 10:
            print('Максимальная длина списка (10) превышена')
            # для того, чтобы выдавать ошибку, а не просто сообщение
            # закомментить строку выше и откомментить строку ниже
            # raise ValueError('Максимальная длина списка (10) превышена')
        else:
            super().__init__(values)
    def append(self, values):
        if len(values) == 10:
            print('Максимальная длина списка (10) превышена')
            # для того, чтобы выдавать ошибку, а не просто сообщение
            # закомментить строку выше и откомментить строку ниже
            # raise ValueError('Максимальная длина списка (10) превышена')
        else:
            super().append(values)

# Подзадание №3: Сделать лист с уникальными элементами (как множество)
class Pseudo_set(list):
    def __init__(self, value = []):
         list.__init__(self)
         self.concat(value)
    def concat(self, value):
         for x in value:
             if not x in self:
                 self.append(x)
    def append(self, value):
        if value in self:
            return self
        else:
            super().append(value)

# тест подзадания №1
x = Pseudo_Int(2)
y = Pseudo_Int(2)
print('x = ', x)
print('y = ', y)
print('x + y = ', x + y)

# тест подзадания №2
my_list = Pseudo_list([1, 2, 3])
my_list = Pseudo_list(my_list + [4, 5, 6, 7, 8, 9, 10, 11, 12])

# тест подзадания №3
my_list = Pseudo_set([1, 1, 3, 6, 5, 5, 6, 8])
print(my_list)                                  # дубли успешно удаляются
my_list.append(8)
print(my_list)                                  # дубли не добавляются
my_list.append(9)
print(my_list)                                  # уники добавляются
