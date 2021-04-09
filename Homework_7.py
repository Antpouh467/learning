# Задание из видео "Python для начинающих 6"
# Подзадание №1: описать классом(-ами) ваши данные
from fuzzywuzzy import fuzz


class Class_Homework7:
    def __init__(
            self,
            name,
            prof,
            exp,
            os,
            height
            ):
        self.name = name
        self.prof = prof
        self.exp = exp
        self.os = os
        self.height = height
        self.key = name

    def __repr__(self):
        return "Search_Class('%s', '%s', %s, '%s', %s)" % (
            self.name,
            self.prof,
            self.exp,
            self.os,
            self.height
            )


anton = Class_Homework7("Антон", "Маркетолог", 0, "Windows", 180)
kirill = Class_Homework7("Кирилл", "Инженер", 1, "Windows", 175)
arsenij = Class_Homework7("Арсений", "Слесарь", 0, "Linux", 182)
# Подзадание №2: Реализовать поиск по полям типа "рост больше 120",
# "имя Наташа"
# Создаем словарь
people = {
    anton.key: anton,
    kirill.key: kirill,
    arsenij.key: arsenij
}
# for x in people:
#     print(people[x].prof)
# реализуем точный поиск
# суть: человек вводит сроку. Первое слово определяет параметр поиска
# допустимые слова: имя / профессия / опыт / ос / рост
# для опыта и роста далее считывается второе слово: больше / меньше
# если нет - значит "равно"
# последнее слово будет значением поиска

# составим запросы заранее
queries = [
    'рост 180',
    'имя кирил',
    'профессия инженер',
    'опыт 2',
    'ос Linux',
    'рост меньше 180',
    'опыт больше 0'
    ]


# используем метод find()
# не используем здесь оператор "in", т.к. значение "ос " может найтись не
# в начале строки. Оставляем его на остальное
# общая структура:
#     - ищем имя?
#         если да, то обрезаем строку до значения для поиска
#         и сравниваем это с соответствующими параметрами каждого элемента
#     - ищем профессию?
#         аналогично имени
#     - ищем опыт?
#         - Определяем, надо ли "больше", "меньше" или "равно"
#             обрезаем строку до значения для поиска
#             и сравниваем это с соответствующими параметрами каждого элемента
#     - ищем ОС?
#         аналогично имени
#     - ищем рост?
#         аналогично профессии
# в сравниваемых в рамках "if" значениях есть пробелы - это чуть более
# сильное сравнение, только для этого

with open('Homework_7_results.txt', 'w') as f:
    for find_input in queries:
        exact_people = {}
        print('Запрос (точный): ', find_input, file=f)
        if find_input.find("имя ") == 0:
            # find_value - обрезанная строка (включая пробел после параметра
            # поиска)
            find_value = find_input[4:]
            for person in people:
                if people[person].name == find_value:
                    exact_people[person] = people[person]
        elif find_input.find("профессия ") == 0:
            find_value = find_input[10:]
            for person in people:
                if people[person].prof == find_value:
                    exact_people[person] = people[person]
        elif find_input.find("опыт ") == 0:
            if find_input.find(" больше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].exp > find_value:
                        exact_people[person] = people[person]
            elif find_input.find(" меньше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].exp < find_value:
                        exact_people[person] = people[person]
            else:
                find_value = int(find_input[5:])
                for person in people:
                    if people[person].exp == find_value:
                        exact_people[person] = people[person]
        elif find_input.find("ос ") == 0:
            find_value = find_input[3:]
            for person in people:
                if people[person].os == find_value:
                    exact_people[person] = people[person]
        elif find_input.find("рост ") == 0:
            if find_input.find(" больше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].height > find_value:
                        exact_people[person] = people[person]
            elif find_input.find(" меньше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].height < find_value:
                        exact_people[person] = people[person]
            else:
                find_value = int(find_input[5:])
                for person in people:
                    if people[person].height == find_value:
                        exact_people[person] = people[person]
        print("Найденные люди:", file=f)
        print(exact_people, file=f)
        print('', file=f)

# Подзадание №3: Сделать поиск нечетким, наташа = нташа = Наташа;
# 120 = 121 = 118
# будем использовать фузивузи для строк, +-3 для чисел, но только "равно"

# with open('out.txt', 'w') as f:
#     print('Filename:', filename, file=f)
    for find_input in queries:
        exact_people = {}
        print('Запрос (неточный): ', find_input, file=f)
        if find_input.find("имя ") == 0:
            # find_value - обрезанная строка (включая пробел после параметра
            # поиска)
            find_value = find_input[4:]
            for person in people:
                if fuzz.WRatio(people[person].name, find_value) > 67:
                    exact_people[person] = people[person]
        elif find_input.find("профессия ") == 0:
            find_value = find_input[10:]
            for person in people:
                if fuzz.WRatio(people[person].prof, find_value) > 67:
                    exact_people[person] = people[person]
        elif find_input.find("опыт ") == 0:
            if find_input.find(" больше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].exp > find_value:
                        exact_people[person] = people[person]
            elif find_input.find(" меньше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].exp < find_value:
                        exact_people[person] = people[person]
            else:
                find_value = int(find_input[5:])
                for person in people:
                    if abs(people[person].exp - find_value) < 4:
                        exact_people[person] = people[person]
        elif find_input.find("ос ") == 0:
            find_value = find_input[3:]
            for person in people:
                if fuzz.WRatio(people[person].os, find_value) > 67:
                    exact_people[person] = people[person]
        elif find_input.find("рост ") == 0:
            if find_input.find(" больше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].height > find_value:
                        exact_people[person] = people[person]
            elif find_input.find(" меньше ") != -1:
                find_value = int(find_input[12:])
                for person in people:
                    if people[person].height < find_value:
                        exact_people[person] = people[person]
            else:
                find_value = int(find_input[5:])
                for person in people:
                    if abs(people[person].height - find_value) < 4:
                        exact_people[person] = people[person]
        print("Найденные люди:", file=f)
        print(exact_people, file=f)
        print('', file=f)

# return "test"# search_result
# pprint(anton.height)
