# Задание из видео "Python для начинающих 12"
# Подзадание №1: В терминах ООП описать предметную область, которую вы ранее
# писали словарем
# Подзадание №2: Придумать по 2-3 действия каждому представителю
# Подзадание №3: Обосновать в комментариях, почему именно такая структара
# выбрана и такие имена даны
# =============================================================================
# Суть: у нас есть список людей с определенными переменными. Среди них
# рост и имя особо изменяться не будут, а ОС не так важна, как опыт работы
# и профессия. Отсюда у нас и определяющая класс объекта - профессия.
# У разных профессий у нас разная зп, место работы, тип работы и коэффициент
# прибавки к зп. Не меняются у нас рост (который не надо запихивать в функцию)
# и ОС. Формулу зарплаты мы тоже можем привести к общему знаменателю.
# Исходя из этого, мы можем создать общий родительский класс для всех людей
# People с этими переменными и функциями, и дочерние классы по профессиям
# Marketer, Engeneer и Locksmith. Названия их методов достаточно очевидны -
# в основном это глаголы для чего этот метод нужен, или название параметра
# который рассчитывается (salary, exp_factor)
# =============================================================================
class People:
    def __init__():          # - Конструктор с полями
        pass
    def change_os():         # - Смена ОС, общая для всех
        pass
    def salary():            # - Калькулятор зп, для безработных и без опыта
        pass                 # минималка
    
class Marketer:              # - Класс маркетолога. Наследует имя, ОС и рост
    def __init__():
        pass
    def _increase_exp():     # - Увеличение опыта. Содержит в себе нижнее
        pass                 # подчеркивание, т.к. это внутренняя функция,
                             # которая не должна вызываться извне, а только
                             # лишь при вызове функции work
    def go_to_work():        # - Идти на работу. Может быть разным местом в
        pass                 # зависимости от профессии
    def work():              # - Команда работать, включает запрос "сколько"
        pass                 # влияет на получение опыта.
                             # Есть только у работающих людей, поэтому
                             # присутствует только у классов профессий
    def exp_factor():        # - Метод для определения коэффициента опыта
        pass                 # Больше опыт -> больше зп. Зависит от профессии

class Engeneer:              # - Все аналогично маркетологу, повторять не буду
    def __init__():
        pass
    def _increase_exp():
        pass
    def go_to_work():
        pass
    def work():
        pass
    def exp_factor():
        pass
    
class Locksmith:
    def __init__():
        pass
    def _increase_exp():
        pass
    def go_to_work():
        pass
    def work():
        pass
    def exp_factor():
        pass