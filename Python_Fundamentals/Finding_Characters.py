# Write a program that takes a list of strings and a string containing a single character,
# and prints a new list of all the strings containing that character.
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
char1 = 'e'
char2 = 'n'

def Find_character(lst, substring):
    new_list = []
    for element in lst:
        if substring in element:
            new_list.append(element)
    print new_list

Find_character(word_list, char)
Find_character(word_list, char1)
Find_character(word_list, char2)
# print filter(lambda x: char in x, word_list)

# This is What I Started Out with:
# for i in range (0, len(word_list)-1):
#     if word_list[i].find(char) >=0:
#         new_list += word_list[i]
#         print new_list
# output
# new_list = ['h','e','l','l','o','w','o','r','l','d']
# not the correct answer
