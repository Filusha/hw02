# Task 01.
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
vl_type_list = ["Char", 7, 4.28, (2 + 0.7j),  ( 3, 4.5, "txt", True ), range(9), {"name" : "Ivan", "age" : 16}, { "memvar", "operator", "statement"}, frozenset(), True, b"byte", bytearray(3), memoryview(bytes(5)), None]

vn_cnt = 0
for i in vl_type_list:
    vn_cnt += 1
    print( str(vn_cnt) + " -- ", i, type(i), end = "\n" )
