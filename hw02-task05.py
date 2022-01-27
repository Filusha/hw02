# Task 05.
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
# 

vl_rating = [7, 6, 5, 3, 2]
vn_number = 0
print(vl_rating)
while True:
    vs_input = input("Enter natural number, q for quit: ")
    if vs_input == "q":
        break
    elif not vs_input.isdigit():
        print("Please enter q for quit or natural number")
    else:
        vn_input = int(vs_input)
#        vn_len = len(vl_rating)
        if vn_input in vl_rating:
            vn_pos = vl_rating.index(vn_input)
            vn_cnt = vl_rating.count(vn_input)
            vl_rating.insert(vn_pos + vn_cnt,  vn_input)
        else:
            vl_rating.append(vn_input)
            vl_rating.sort(reverse=True)
        print(vl_rating)

