# Task 04.
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
#

vl_words = input("Enter a few words. Use space as a delimiter: ").split()
for I, word in enumerate(vl_words, 1):
    print(f"{I} {word[:10]}")
