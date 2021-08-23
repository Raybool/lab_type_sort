import random as r
# Вариант 4 (1, 5, 6)
"""
1)    Обменная сортировка (метод пузырька);
5)    Метод Шелла;
6)    Быстрая сортировка.
"""


def exchange_sort(a, a_len):  # метод пузырька
    for num in range(1, a_len + 1):
        i = a_len - 1
        while i != num - 1:
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a


def shell_method(a_array, n):  # метод Шелла
    a = [9, 5, 3, 2, 1]
    for k in range(5):
        gap = a[k]
        for i in range(gap, n):
            temp = a_array[i]
            j = i - gap
            while temp < a_array[j] and j >= 0:
                a_array[j + gap] = a_array[j]
                j -= gap
            a_array[j + gap] = temp
    return a_array


def quick_sort(a, first_n, last_n):    # быстрая сортировка
    if first_n >= last_n:
        return
    p = a[r.randint(first_n, last_n)]
    i = first_n
    j = last_n
    while i <= j:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    quick_sort(a, first_n, j)
    quick_sort(a, i, last_n)
