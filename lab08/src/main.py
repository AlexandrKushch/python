def count_lines(file_name):
    try:
        with open(file_name, 'r') as f:
            i = 0
            for line in f:
                print(i, 'line:', len(line.rstrip()))
                i += 1
    except FileNotFoundError as e:
        print(e)


def remove_change(file_name, file_result_name, remove=-1, change1=-1, change2=-1):
    try:
        with open(file_name, "r") as f:
            with open(file_result_name, "w") as fr:
                i = 0
                str1, str2 = "", ""

                for line in f:
                    if i is change1:
                        str1 = line
                    if i is change2:
                        str2 = line
                    i += 1

                i = 0
                f.seek(0)

                for line in f:
                    if line == str1:
                        fr.write(str2)
                        continue
                    if line == str2:
                        fr.write(str1)
                        continue
                    if i is not remove:
                        fr.write(line)
                    i += 1
    except FileNotFoundError as e:
        print(e)


filename = "1.txt"
file_result = "2.txt"
count_lines(filename)

remove_change(filename, file_result, change1=1, change2=4, remove=3)
