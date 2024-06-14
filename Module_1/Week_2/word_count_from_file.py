import re

def word_count (file_path):
    lst_word = []
    dict_word = {}
    with open(file_path, "r") as file:
        string = file.read()
        lst_word = re.split(r'[ \n]', string)
        for i in lst_word:
            dict_word[i] = lst_word.count(i)
    file.close
    print (dict_word)

#test
file_path = 'Module_1/Week_2/P1_data.txt'
word_count(file_path)
