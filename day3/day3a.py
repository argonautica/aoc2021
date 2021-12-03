with open("input.txt") as file:
    t = file.read().split()

temp = [0 for _ in range(len(t[0]))]
# print(temp)
for a in range(len(t)):
    for j in range(len(t[a])):
        if (t[a][j] == "1"):
            temp[j] += 1


g = ""
e = ""
for j in temp:
    if (j > len(t)-j):
        g += "1"
        e += "0"
    else:
        e += "1"
        g += "0"
print(int(g, 2) * int(e, 2))