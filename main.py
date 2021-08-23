import test as t
import random as r


def input_len():  # функция ввода длинны массива
    return int(input("Введите длинну последовательности: "))


def array_sorted_test(col_num):  # функция создание сортированного массива
    a = list()
    for n in range(0, col_num):
        a.append(n)
    return a


def array_random_test(col_num):  # функция создания рандомного массива
    a = list()
    for n in range(col_num):
        a.append(r.randint(0, 200))
    return a


def array_reverse_test(col_num):  # функция создания обратного массива
    a = list()
    z = col_num - 1
    for n in range(col_num):
        a.append(z)
        z -= 1
    return a


def printing(message):  # функция вывода
    f = open("output.txt", "w")
    f.write(message)
    f.close()


#   Основная программа
array_len = input_len()
array_sorted = array_sorted_test(array_len)
array_random = array_random_test(array_len)
array_reverse = array_reverse_test(array_len)

# вывод в таблице
text = "Количество элементов: %d\n" % array_len
text = text + ("Случайная последовательность, сгенерированная программно: " + str(array_random) + "\n")
text = text + "|%-22s|%-15s|%-15s|%-35s|\n" % ("Метод", "Отсортированная", "Случайная", "Отсортированная в обратном порядке")
t_sort, t_rand, t_rev = t.test_exchange_sort(array_sorted, array_random, array_reverse, array_len)
text = text + "|%-22s|%-15f|%-15f|%-35f|\n" % ("Метод пузырька", t_sort, t_rand, t_rev)
t_sort, t_rand, t_rev = t.test_shell_method(array_sorted, array_random, array_reverse, array_len)
text = text + "|%-22s|%-15f|%-15f|%-35f|\n" % ("Метод Шелла", t_sort, t_rand, t_rev)
t_sort, t_rand, t_rev = t.test_standard_sort(array_sorted, array_random, array_reverse)
text = text + "|%-22s|%-15f|%-15f|%-35f|\n" % ("Стандартная сортировка", t_sort, t_rand, t_rev)
t_sort, t_rand, t_rev = t.test_quick_sort(array_sorted, array_random, array_reverse, array_len)
text = text + "|%-22s|%-15f|%-15f|%-35f|\n" % ("Быстрая сортировка", t_sort, t_rand, t_rev)
printing(text)

