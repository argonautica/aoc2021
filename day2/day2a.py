with open("input.txt") as file:
    t = [a.split() for a in file.readlines()]

x = 0
y = 0
for a in t:
    if (a[0] == "forward"):
        x += int(a[1])
    elif (a[0] == "up"):
        y -= int(a[1])
    else:
        y += int(a[1])
print(y*x)