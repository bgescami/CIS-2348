# Brandon Escamilla PSID:1823960
#
# Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method.
# The file contains a list of words separated by commas. Your program should output the words and their frequencies
# (the number of times each word appears in the file) without any duplicates.
#
# You will need to import the csv module.
#
# Ex: If the input is:
#
# input1.csv
# and the contents of input1.csv are:
#
# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:
#
# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1
# Note: There is a newline at the end of the output, and input1.csv is available to download.


import csv

#getting the input
input1 = input()

#opening the file from user input
with open(input1, 'r') as wordsfile:
    #reading the data from the file
    words_reader = csv.reader(wordsfile)
    #starting to loop through all data no matter if there is repitition.
    for row in words_reader:
        list_of_words = row

#eliminate duplicates
no_duplicates_in_list = list(dict.fromkeys(list_of_words))
#creating a single list
listlength = len(no_duplicates_in_list)

#counting how many of each word
for i in range(listlength):
    print(no_duplicates_in_list[i], list_of_words.count(no_duplicates_in_list[i]))



