sentence = input()

sentence = sentence.strip()
sentence = sentence.replace("-", " ")

if sentence.count(" ") > 10:
    print("Count of words should less than 10")
else:
    print(sentence)

    array = sentence.split()
    result = ""

    for i in array:
        if sentence.count(i) == 1:
            result += i + " "

    result = result.strip()
    print(result)
