import random

n = 15
surnames = [''] * n
heights = random.sample(range(160, 200), n)

for i in range(n):
    surnames[i] = "st" + str(i+1)

students = dict()
for i in range(n):
    students[surnames[i]] = heights[i]

print(students)

# -------------------1-----------
min_st = min(students.keys(), key=(lambda k: students[k]))
print('Min:', min_st)
max_st = max(students.keys(), key=(lambda k: students[k]))
print('Max:', max_st)

# ---------------------2------------
deleted = {}
deleted[max_st] = students.pop(max_st)

second_st = max(students.keys(), key=(lambda k: students[k]))

deleted[second_st] = students.pop(second_st)

third_st = max(students.keys(), key=(lambda k: students[k]))

print("Second and Third tall student:", second_st, third_st)

for i in deleted.keys():
    students[i] = deleted[i]

# ---------------------3------------

first = min_st
second = min_st

for i in students:
    if students[i] > students[first]:
        second = first
        first = i

print("First and Second student(One loop):", first, second)

print(students)

