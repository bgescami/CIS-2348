#Brandon Escamilla PSID: 1823960
#ZyLab 11.22

words = input().split()
for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, count)