# Brandon Escamilla PSID: 1823960
#
# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing
# characters using the key below, and by appending "q*s" to the end of the input string.
#
# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .

#gets original password from input
word = input()

#each line is editing and replacing.
word = word.replace('i', '!')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('o', '.')
#there is no replacing for this step, so we are just adding a string to the end of our new word.
word += 'q*s'

print(word)