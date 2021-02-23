import random

print("N and M value")
n = int(input())
m = int(input())

array = [0] * n
for i in range(n):
    array[i] = [0] * m

for i in range(n):
    for j in range(m):
        array[i][j] = random.uniform(-10, 10)

print("Default:")
for i in array:
    for j in i:
        print(j, end=" ")
    print()

minimum = array[0][0]
minimum_key = 0

for i in range(n):
    for j in range(m):
        if array[i][j] >= 0:
            if minimum > array[i][j]:
                minimum = array[i][j]
                minimum_key = j

print("MinElem:", minimum, "Column", minimum_key)

for i in range(m):
    array[i][minimum_key], array[i][len(array) - 1] =\
        array[i][len(array) - 1], array[i][minimum_key]

print("Replaced:")

for i in array:
    for j in i:
        print(j, end=" ")
    print()