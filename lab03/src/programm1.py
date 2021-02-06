import random


print("Enter the length of list")
n = int(input())

array = [0] * n
new_array = []

for i in range(n):
    array[i] = random.randint(-60, 60)

print(*array, sep=", ")
print("Enter x and y")

x = int(input())
y = int(input())

for i in array:
    if i >= 0:
        if x <= i <= y:
            new_array += [i]
    else:
        break

print("New Array")
print(*new_array, sep=", ")
print("Length of New Array", len(new_array))
