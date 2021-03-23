import random


def qsort(array, fst, lst):
    """
    Сортує масив використовуючи алгоритм швидкого сортування

    :param array: Масив з вхідними даними
    :param fst: Перший елемент
    :param lst: Останній елемент
    :return: Вихід з функції якщо пеший та останній елементи однакові
    """

    if fst >= lst:
        return

    p = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    qsort(array, fst, j)
    qsort(array, i, lst)


def find(array, value):
    """
    Пошук першого подібного елементу за переданим значенням

    :param array: Масив з вхідними даними
    :param value: Значення елементу яке шукаємо
    :return: Повертаємо порядковий номер елменту в масиів
    """

    for i in range(len(array)):
        if array[i] == value:
            return i


def n_elems(array, n, reverse=0):
    """
    Пошук перших 'n' елементів мінімуму або максимуму, в залежності від 'reverse'

    :param array: Масив з вхідними даними
    :param n: Кількість елементів для пошуку
    :param reverse: 0 - мінімум, 1 - максимум
    :return: Повертаємо результуючий масив з 'n' елементів
    """

    result = [0] * n

    for i in range(n):
        if reverse == 0:
            min_max = 9999
        else:
            min_max = -9999

        for j in range(len(array)):
            if array[j] not in result:
                if reverse == 0:
                    if array[j] < min_max:
                        min_max = array[j]
                else:
                    if array[j] > min_max:
                        min_max = array[j]
                result[i] = min_max

    return result


def average(array):
    """
    Середнье арифметичне

    :param array: Масив з вхідними даними
    :return: Повертаємо середнье арифметичне
    """
    return sum(array) / len(array)


def list_non_repeat(array):
    """
    Позбавляє масив однакових значень

    :param array: Масив з вхідними даними
    :return: Повертає результат
    """

    return list(set(array))


def pairs(array):
    """
    Пошук кількості  пар чисел, де перше більше наступного

    :param array: Масив з вхідними даними
    :return: Кількість парь
    """

    counter = 0

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            counter += 1

    return counter


mas = [4, 1, 3, 5, 9, 10, 7, 2, 6, 8, 10, 1, 2]
mins = n_elems(mas, 3)
maxs = n_elems(mas, 3, reverse=1)

print("Array Before Sort: ", mas)
print("Mins: ", mins)
print("Maxs: ", maxs)
print("Average: ", average(mas))
print("List without repeats:", list_non_repeat(mas))
print("Pairs: ", pairs(mas))

qsort(mas, 0, int(len(mas) - 1))
print("Array After Sort: ", mas)
