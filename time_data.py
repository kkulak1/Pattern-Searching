import time
import gc

from wyszukiwanie_wzorca import naive, KMP, KR


def get_naive_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        naive(words_to_measure, "Zosia")
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_KMP_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        KMP(words_to_measure, "Zosia")
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_KR_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        KR(words_to_measure, "Zosia", 13)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list
