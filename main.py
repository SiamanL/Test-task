f = input("enter .txt file name\n")
with open("{}.txt".format(f), "r", encoding="utf-8") as file:
    content = file.read()

list = []
word = {}
wr = []
arr = []
_lif = []

for i in content:
    list.append(i)
    if i != "\n":
        wr.append(i)
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    else:
        arr.append(wr)
        _lif.append(word)
        word = {}
        wr = []


if list[-1] != "\n":
    _lif.append(word)
    arr.append(wr)

used = [False] * len(arr)

with open("result.txt", "w", encoding="utf-8") as file:
    for i in range(len(arr)):
        if used[i]:
            continue
        group = [''.join(arr[i])]
        used[i] = True
        for j in range(i + 1, len(arr)):
            if not used[j] and _lif[i] == _lif[j]:
                group.append(''.join(arr[j]))
                used[j] = True
        file.write(' '.join(group))
        if not all(used): file.write("\n")

