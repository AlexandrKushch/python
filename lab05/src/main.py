# --------1---------
text = "hello world im fine and how are you"

text = text.strip()
text = text.replace("-", " ")
text = text.lower()

if text.count(" ") > 10:
    print("I'm so sorry:(")
else:
    array = text.split()
    print(array)
    print(sorted(array, key=len))

# --------2---------
_text = "здоров, світе, я, чудово, як, ся, маєш"
_text = _text.replace(",", "")
print(_text)

vowels = set("аеіїоиуяєю")
consonant = set("бвгджзйклмнпрстфхцчшщ")
_array = _text.split()

for i in _array:
    setText = set(i)

    vowelsText = vowels & setText

    print("In '", i, "' Vowels:", vowelsText)

setText = set(_text)
consonantText = consonant - setText
consonantText = sorted(consonantText)
print("All consonants which didn't in", _text, "is:", consonantText)

# -------3-------
# a)
s = str(set('aeiouy'))
print(s)

# b)
numbers = 12
set_nums = set()

for i in range(numbers):
    set_nums.add(i)

s = str(set_nums)
print(s)

# c)
range_s = {'b', 'x'}
set_str = set()

lst, fst = range_s.pop(), range_s.pop()
if ord(lst) < ord(fst):
    lst, fst = fst, lst

range_s.add(fst)    # If you want to use this in future
range_s.add(lst)

i = ord(fst)

while i <= ord(lst):
    set_str.add(chr(i))
    i += 1

s = str(set_str)
print(s)
