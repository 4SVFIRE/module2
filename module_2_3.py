my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while len(my_list) > 0:
    number = my_list[0]
    my_list.remove(my_list[0])
    if number == 0:
        continue
    elif number >= 1:
        print(number)
    else:
        break
