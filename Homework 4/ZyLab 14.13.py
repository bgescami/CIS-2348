#Brandon Escamilla PSID: 1823960
#ZyLab 14.13

num_calls = 0
# fucntion for partiton


def partition(user_ids, l, h):
    i = (l-1)
    pivot = user_ids[h]

    for j in range(l,h):
        if user_ids[j] <= pivot:
            i = i+1
            user_ids[i],user_ids[j] = user_ids[j],user_ids[i]
    user_ids[i +1],user_ids[h] = user_ids[h],user_ids[i + 1]
    return i + 1

def quicksort(lst, l, h):
    global num_calls
    num_calls = num_calls +1
    if l < h:
        p = partition(lst, l, h)
        quicksort(lst, l, p-1)
        num_calls = num_calls + 1
        quicksort(lst, p + 1, h)

lst = []
while True:
    inp = input()
    if inp == "-1":
        break
    else:
        lst.append(inp)

size = len(lst)
quicksort(lst, 0, size - 1)
print(num_calls)
for i in range(size):
    print(lst[i])
