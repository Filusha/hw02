# Task 03.
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и dict.
# 

vl_list_seasons = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
vd_dict_seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}

while True:
    vs_input = input("Enter month number, q for quit: ")
    if vs_input == "q":
        break
    else:
        vn_requested_month = int(vs_input)
        if 1 <= vn_requested_month <= 12:
            print(vl_list_seasons[vn_requested_month - 1])
            print(vd_dict_seasons[vn_requested_month])
        else:
            print("Invalid month number")
