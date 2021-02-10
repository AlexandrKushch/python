import random

n = 15
surnames = [''] * n
heights = random.sample(range(160, 200), n)

for i in range(n):
    surnames[i] = "st" + str(i+1)

students = dict()
for i in range(n):
    students[surnames[i]] = heights[i]

min = students['st1']
min_key = 'st1'
max = students['st1']
max_key = 'st1'

for i in students:
    if min > students[i]:
        min = students[i]
        min_key = i
    if max < students[i]:
        max = students[i]
        max_key = i

high_students_key = [min_key] * 2
high_students = [students[min_key]] * 2

for i in students:
    if i != max_key:
        if students[i] > high_students[0]:
            high_students[1] = high_students[0]
            high_students_key[1] = high_students_key[0]
            high_students[0] = students[i]
            high_students_key[0] = i

print("Max:", max_key, "Min:", min_key)
print("2&3 High student:", high_students_key)
print(students)
