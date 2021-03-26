# Задание из видео "Python для начинающих 4"
# Подзадание №1: Используя numpy, посчитать сумму ряда 0-100
import numpy
determined_array = numpy.array(range(100))
print(numpy.sum(determined_array))
# Подзадание №2: Используя numpy, посчитать сумму ряда 0-input(100)
undetermined_array = numpy.array(range(int(input())))
print(numpy.sum(undetermined_array))
# Подзадание №3: Используя numpy, посчитать среднее среди 100 случайных чисел
random_array = numpy.random.rand(1,100)
# т.к. не было указано, какой тип чисел, случайные числа от 0 до 1 тоже должны засчитаться
print("Сгенерированные числа: ", random_array)
print("Сумма: ", numpy.mean(random_array))