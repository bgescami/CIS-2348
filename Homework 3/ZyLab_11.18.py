#Brandon Escamilla PSID:1823960
#ZyLab 11.18

numbers = [int(i) for i in input().split()]

sorted_numbers = sorted(numbers)

for i in sorted_numbers:
    if i >= 0:
        print(i, end=' ')

