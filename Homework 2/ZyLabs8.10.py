# Brandon Escamilla PSID: 1823960
#
# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.
#
# Ex: If the input is:
#
# bob
# the output is:
#
# bob is a palindrome
# Ex: If the input is:
#
# bobby
# the output is:
#
# bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

#taking user input. python automatically reads it as a string
word = input()
#now i am replacing each space with no space, so "hi there" turns into "hithere".
str_word = word.replace(' ', '')
#runs with no problem up to this point

#now that we have our input with no spaces, we want to reverse it, which is what i am doing below.
str_sliced = str_word[::-1]

if str_word == str_sliced:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')
