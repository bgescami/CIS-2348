# Brandon Escamilla         PSID#: 1823960
# Enter amount of lemon juice (in cups):
# 2
# Enter amount of water (in cups):
# 16
# Enter amount of agave nectar (in cups):
# 2.5
# How many servings does this make?
# 6
#
# Lemonade ingredients - yields 6.00 servings
# 2.00 cup(s) lemon juice
# 16.00 cup(s) water
# 2.50 cup(s) agave nectar
#
#
#
# How many servings would you like to make?
# 48
#
# Lemonade ingredients - yields 48.00 servings
# 16.00 cup(s) lemon juice
# 128.00 cup(s) water
# 20.00 cup(s) agave nectar
#
#
#
# Lemonade ingredients - yields 48.00 servings
# 1.00 gallon(s) lemon juice
# 8.00 gallon(s) water2
# 1.25 gallon(s) agave nectar


# getting the info as input and then turning it into an integer
lem = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serv = float(input("How many servings does this make?\n\n"))

print("Lemonade ingredients - yields",'{:.2f}'.format(serv), "servings")
print("{:.2f}".format(lem), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(agave), "cup(s) agave nectar\n")


# now to see how many servings we need to make (think mathematically of ratios)
nserv = float(input("How many servings would you like to make?\n\n"))
ratio = nserv / serv
print("Lemonade ingredients - yields",'{:.2f}'.format(nserv), "servings")
print("{:.2f}".format(lem * ratio), "cup(s) lemon juice")
print("{:.2f}".format(water * ratio), "cup(s) water")
print("{:.2f}".format(agave * ratio), "cup(s) agave nectar\n")


# now to convert to gallons
# I did the math inside of the format function. The insides solve first, and then the answer is formatted.
print("Lemonade ingredients - yields",'{:.2f}'.format(nserv), "servings")
print("{:.2f}".format((lem * ratio)/16), "gallon(s) lemon juice")
print("{:.2f}".format((water * ratio)/16), "gallon(s) water")
print("{:.2f}".format((agave * ratio)/16), "gallon(s) agave nectar")