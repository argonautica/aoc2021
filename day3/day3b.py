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


t2 = t
t3 = t
for j in range(len(temp)):
    print(t2)
    if (len(t2) == 1):
        g = t2[0]
        break
    print(temp[j], len(t))
    if (temp[j] >= len(t) - temp[j]):
        t2 = [a for a in t2 if str(a)[j] == "1"]
    else:
        t2 = [a for a in t2 if str(a)[j] == "0"]

print(temp)
for j in range(len(temp)):
    if (len(t3) == 1):
        e = t3[0]
        break
    if (temp[j] >= len(t) - temp[j]):
        t3 = [a for a in t3 if str(a)[j] == "0"]
    else:
        t3 = [a for a in t3 if str(a)[j] == "1"]





print(g, e)
