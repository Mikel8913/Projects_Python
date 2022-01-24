import math

# Создать переменную item_1 типа integer.
# Создать переменную item_2 типа integer.
# Создать переменную result_sum в которой вы суммируете item_1 и item_2.
# Вывести result_sum в консоль.

item_1 = 3
item_2 = 9
result_sum = item_1 + item_2
print(result_sum)

# Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
# Вывести result_subtr в консоль.

result_subtr = item_2 - item_1
print(result_subtr)

# Создать переменную result_multi в которой вы умножаете item_1 на item_2.
# Вывести result_multi в консоль.

result_multi = item_1 * item_2
print(result_multi)

# Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
# Вывести result_exp в консоль.

result_exp = item_1 ** item_2
print(result_exp)

# Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
# Вывести result_m_exp в консоль.

result_m_exp = math.pow(item_1, item_2)
print(result_m_exp)

# Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item.
# Вывести result_s_root в консоль.

result_s_root = item_2 ** (0.5)
print(result_s_root)

# Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
# Вывести result_m_s_root в консоль.

result_m_s_root = math.sqrt(item_2)
print(result_m_s_root)

# Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
# Вывести result_mp_s_root в консоль.

result_mp_s_root = pow(item_2, 0.5)
print(result_mp_s_root)

# Присвоить переменной item_1 odd значение
# Присвоить переменной item_2 even значение
# Создать переменную result_division в которой вы разделите item_1 на item_2.
# Вывести result_division в консоль.

item_1 = 33
item_2 = 16
result_division = item_1 / item_2
print(result_division)

# Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
# Вывести result_m_floor в консоль.

result_m_floor = math.floor(result_division)
print(result_m_floor)

# Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
# Вывести result_m_ceil в консоль.

result_m_ceil = math.ceil(result_division)
print(result_m_ceil)

# Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
# Вывести result_int в консоль.

result_int = int(round(result_division))
print(result_int)

# Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
# Вывести result_no_division_loss в консоль.

result_no_division_loss = item_1 // item_2
print(result_no_division_loss)

# Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
# Вывести result_division_loss в консоль.

result_division_loss = item_1 % item_2
print(result_division_loss)

# Создать переменную item_3 и присвоить ей целое число
# Прибавить 10 к item_3 с присвоением.
# Вывести item_3 в консоль.

item_3 = 12
item_3 += 10
print(item_3)

# Отнять 5 от item_3 с присвоением.
# Вывести item_3 в консоль.

item_3 -= 5
print(item_3)

# Умножить item_3 на 3 с присвоением.
# Вывести item_3 в консоль.

item_3 *= 3
print(item_3)

# Разделить item_3 на 2 с присвоением.
# Вывести item_3 в консоль.

item_3 /= 2
print(item_3)

# Возвести в степень 2 item_3 с присвоением.
# Вывести item_3 в консоль.

item_3 **= 2
print(item_3)

# Найти квадратный корень item_3 с присвоением.
# Вывести item_3 в консоль.

item_3 **= 0.5
print(item_3)

# Присвоить остаток от деления item_3
# Вывести item_3 в консоль.

item_3 %= 2
print(item_3)

                                       # Boolean
# Создать переменную b_item_t и присвоить True
# Создать переменную b_item_f и присвоить False
# Создать переменную b_item_result_sum и присвоить сумму b_item_t и b_item_f
# Вывести b_item_relult_sum в консоль.

b_item_t = True
b_item_f = False
b_item_result_sum = b_item_t + b_item_f
print(b_item_result_sum)

# Создать переменную b_item_result_subtr и присвоить разницу b_item_t и b_item_f
# Вывести b_item_relult_subtr в консоль.

b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)

# Создать переменную b_item_result_multi и присвоить умножение b_item_t и b_item_f
# Вывести b_item_relult_multi в консоль.

b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)

# Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# Вывести b_item_relult_division в консоль. (Получить ошибку)

try:
    b_item_result_division = b_item_t / b_item_f
    print(b_item_result_division)
except ZeroDivisionError:
    print("Ошибка!!!!!")

# Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
# Вывести b_item_1_int в консоль.

b_item_1_int = int(b_item_t)
print(f" Ответ: {b_item_1_int}")

# Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
# Вывести b_item_2_int в консоль.

b_item_2_int = int(b_item_f)
print(f" Ответ: {b_item_2_int}")