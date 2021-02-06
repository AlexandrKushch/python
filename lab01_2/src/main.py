import math

if __name__ == '__main__':
    #------------1------------
    print('Enter x value: ')
    x = int(input())

    numerator = math.sqrt(math.pow(3 * x + 2, 2) - 24 * x)
    denominator = 3 * math.sqrt(x) - 2 / math.sqrt(x)

    z = numerator / denominator
    print(z)
    #-----------2------------
    print("Enter n value: ")
    n = int(input())
    num = 1
    sum = 0

    while num < n:
        if n % num == 0:
            sum += num
        num += 1

    if sum > n:
        print(sum, " > ", n, " -> excess")
    else:
        print(sum, " < ", n, " -> lack")
