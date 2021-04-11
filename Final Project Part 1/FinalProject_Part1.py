#Brandon Escamilla PSID: 1823960
#Final Project Part 1

import csv
import operator

#part a. Full Inventory
file1 = open('FullInventory.csv', "r")

csv_read1 = csv.reader(file1, delimiter=",")

sort1 = sorted(csv_read1, key=operator.itemgetter(1))

print("\n                 ~FULL INVENTORY~")
for eachline in sort1:
    print(eachline)


#part b. item type inventory list

file2 = open('LaptopInventory.csv', "r")

csv_read2 = csv.reader(file2, delimiter=",")

sort2 = sorted(csv_read2, key=operator.itemgetter(0))

print("\n           ~LAPTOP INVENTORY~")
for eachline in sort2:
    print(eachline)

#part c.
file3 = open('PastServiceDateInventory.csv', "r")

csv_read3 = csv.reader(file3, delimiter=",")

sort3 = reversed(sorted(csv_read3, key=operator.itemgetter(4)))

print("\n         ~PAST SERVICE DATE INVENTORY~")
for eachline in sort3:
    print(eachline)

#part d.
file4 = open('DamagedInventory.csv', "r")

csv_read4 = csv.reader(file4, delimiter=",")

sort4 = sorted(csv_read4, key=operator.itemgetter(4))

print("\n              ~DAMAGED INVENTORY~")
for eachline in sort4:
    print(eachline)
