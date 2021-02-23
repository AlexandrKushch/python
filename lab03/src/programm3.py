sentence = input()

sentence = sentence.strip()
sentence = sentence.replace("-", " ")

if sentence.count(" ") > 10:
    print("Count of words should less than 10")
else:
    array = sentence.split()
    result = ""
    count = 0

    for i in array:
        for j in array:
            if i == j:
                count += 1
        if count == 1:
            result += i + ' '
        count = 0

    result = result.strip()
    print(result)
