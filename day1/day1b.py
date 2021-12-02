with open("input.txt") as file:
    t = [int(a) for a in file.read().split()]

count = 0

temp = []

for j in range(2, len(t)):
    temp.append(t[j] + t[j-1] + t[j-2])

for a in range(1, len(temp)):
    if (temp[a] > temp[a-1]):
        count+= 1
print(count)