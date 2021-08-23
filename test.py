import time
import sorts
# ФУНКЦИИ ДЛЯ ТЕСТОВ


def cheek_array(name, name_arr, arr, array_len):
    flag = True
    for i in range(0, array_len-1):
        if arr[i] > arr[i+1]:
            flag = False
    print("Test %s:" % str(name), "on", str(name_arr), flag)
    if not flag:
        print(arr)


def test_exchange_sort(a_sort, a_rand, a_rev, arr_len):  # функция теста метода пузырька
    time_start = time.time()
    array = sorts.exchange_sort(a_sort, arr_len)
    t_stop_sort = time.time() - time_start
    cheek_array("exchange_sort", "Sort", array, arr_len)
    time_start = time.time()
    array = sorts.exchange_sort(a_rand, arr_len)
    t_stop_rand = time.time() - time_start
    cheek_array("exchange_sort", "Random", array, arr_len)
    time_start = time.time()
    array = sorts.exchange_sort(a_rev, arr_len)
    t_stop_rev = time.time() - time_start
    cheek_array("exchange_sort", "Reverse", array, arr_len)
    return t_stop_sort, t_stop_rand, t_stop_rev


def test_shell_method(a_sort, a_rand, a_rev, arr_len):  # функция теста метода Шелла
    time_start = time.time()
    array = sorts.shell_method(a_sort, arr_len)
    t_stop_sort = time.time() - time_start
    cheek_array("shell_method", "Sort", array, arr_len)
    time_start = time.time()
    array = sorts.shell_method(a_rand, arr_len)
    t_stop_rand = time.time() - time_start
    cheek_array("shell_method", "Random", array, arr_len)
    time_start = time.time()
    array = sorts.shell_method(a_rev, arr_len)
    t_stop_rev = time.time() - time_start
    cheek_array("shell_method", "Reverse", array, arr_len)
    return t_stop_sort, t_stop_rand, t_stop_rev


def test_quick_sort(a_sort, a_rand, a_rev, arr_len):  # функция теста быстрой сортировки
    time_start = time.time()
    array = sorts.quick_sort(a_sort, 0, arr_len-1)
    t_stop_sort = time.time() - time_start
    cheek_array("quick_sort", "Sort", a_sort, arr_len)
    time_start = time.time()
    array = sorts.quick_sort(a_rand, 0, arr_len-1)
    t_stop_rand = time.time() - time_start
    cheek_array("quick_sort", "Random", a_rand, arr_len)
    time_start = time.time()
    array = sorts.quick_sort(a_rev, 0, arr_len-1)
    t_stop_rev = time.time() - time_start
    cheek_array("quick_sort", "Reverse", a_rev, arr_len)
    return t_stop_sort, t_stop_rand, t_stop_rev


def test_standard_sort(a_sort, a_rand, a_rev):
    time_start = time.time()
    array = sorted(a_sort)
    t_stop_sort = time.time() - time_start
    time_start = time.time()
    array = sorted(a_rand)
    t_stop_rand = time.time() - time_start
    time_start = time.time()
    array = sorted(a_rev)
    t_stop_rev = time.time() - time_start
    return t_stop_sort, t_stop_rand, t_stop_rev
