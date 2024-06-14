def count_num_character(str):
    lst_character = []
    dict_numchar = {}
    for i in str:
        lst_character.append(i)

    for i in lst_character:
        dict_numchar[i] = lst_character.count(i)
    print(dict_numchar)


# test
string = 'Happiness'
count_num_character(string)
