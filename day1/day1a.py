with open("input.txt") as file:
    t = [int(a) for a in file.read().split()]

count = 0

for j in range(1, len(t)):
    if (t[j] > t[j-1]):
        count+= 1
print(count)