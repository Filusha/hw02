# Task 02.
# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При 
# нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
#

vl_elements = list(input("Enter elements: "))
print("initial sequence: ", vl_elements)
for I in range(1, len(vl_elements), 2):
    vl_elements[I-1], vl_elements[I] = vl_elements[I], vl_elements[I-1]

print("  final sequence: ", vl_elements)
