# Подзадание №1: Заменить все буквы "x" на "y"
input_line = input("Введите строку для замены:")
output_line = "";
# создали пустую строку для замены
for i in input_line: # проходим по элементам строки
    if i == "x":
        output_line += "y"
    else:
        output_line += i
print("Строка после замены: ", output_line)
print("-----------")

# Подзадание №2: Сосчитать произведение чисел, кратных 3 и 5
init_list_of_numbers = []
result_mult = 1
for i in range(int(input("Количество чисел, из которых надо будет перемножить кратные 3 и 5: "))):
    init_list_of_numbers.append(int(input()))
for i in init_list_of_numbers:
    if i // 3 == i / 3 and i // 5 == i / 5:
        print("Число, кратное 3 и 5: ", i)
        result_mult *= i
print("Получившееся произведение: ", result_mult)
print("-----------")

# Подзадание №3: Заменить буквы в исходной строке без использования дополнительной
print("Замена x на y в строке другим способом:")
print("Исходная строка: ", input_line)
input_line = input_line.replace("x", "y")
print("Преобразованная строка: ", input_line)
