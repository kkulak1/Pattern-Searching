import time
import gc
from matplotlib import pyplot as plt
from random import randint, choice

from wyszukiwanie_wzorca import naive, KMP, KR


def get_naive_time(words):
    time_list = []
    for i in range(10):
        words_to_find = words[:(i+1)*100]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        for word in words_to_find:
            naive(words, word)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_KMP_time(words):
    time_list = []
    for i in range(10):
        words_to_find = words[:(i+1)*100]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        for word in words_to_find:
            KMP(words, word)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_KR_time(words):
    time_list = []
    for i in range(10):
        words_to_find = words[:(i+1)*100]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        for word in words_to_find:
            KR(words, word, 13)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def plot_find_time(time_tab_N, time_tab_KMP):
    tab_of_elements = [x*100 for x in range(1, 11)]

    fig, ax = plt.subplots()
    ax.plot(tab_of_elements, time_tab_N, label="N")
    ax.plot(tab_of_elements, time_tab_KMP, label="KMP")
    # ax.plot(tab_of_elements, time_tab_KR, label="KR")
    ax.set_xlabel("elements")
    ax.set_ylabel("time")
    ax.set_title("Finding time")
    ax.legend()

    plt.savefig("find_time.png")


def random_text_and_pattern():
    text = ""
    pattern = ""

    for i in range(randint(1, 20)):
        text += choice(["A", "B"])

    for i in range(randint(1, 5)):
        pattern += choice(["A", "B"])

    return text, pattern
