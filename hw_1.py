# создать переменные
# String
str_st = "Hello_Python"
# Integer
int_1 = 1
# Float
fl = 1.11
# Bytes
by = b'Hi python'
# List
li = [1, "msi", 1650]
# Tuple
tuple_1 = (11, 33, 44)
# Set
set_1 = set("dog")
# Frozen set
frozen_set = frozenset('qw')
# Dict
dict_1 = {"key": 1}
# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(str_st, type(str_st))
print(int_1, type(int_1))
print(fl, type(fl))
print(by, type(by))
print(li, type(li))
print(tuple_1, type(tuple_1))
print(set_1, type(set_1))
print(frozen_set, type(frozen_set))
print(dict_1, type(dict_1))
# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str_1 = "Go"
str_2 = "Home"
str_3 = str_1 + str_2
print(str_3)
# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(f"{str_st} , {int_1}")
#  Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(f"{str_st} + {int_1}")

