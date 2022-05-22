import time_data
import argparse
import sys


def open_file(path):
    with open(path, "r") as handle:
        words = read_txt(handle)
    return words


def read_txt(handle):
    words = []
    for line in handle:
        if line.isspace():
            continue
        for word in line.split():
            words.append(word.lower())
    return words


def naive(text, patern):
    if not text or not patern:
        return None
    if len(patern) > len(text):
        return None

    ret = []
    t = len(text)
    p = len(patern)

    for i in range(t-p+1):
        j = 0

        while(j < p):
            if (text[i+j] != patern[j]):
                break
            j += 1

        if (j == p):
            ret.append(i)

    return ret


def KMP(text, patern):
    if not text or not patern:
        return None
    if len(patern) > len(text):
        return None

    ret = []
    t = len(text)
    p = len(patern)

    lps = [0]*p  # longest prefix sufix
    j = 0  # index for patern[]

    computerLPSArray(patern, p, lps)

    i = 0  # index for txt[]
    while i < t:
        if patern[j] == text[i]:
            i += 1
            j += 1

        if j == p:
            ret.append(i-j)
            j = lps[j-1]

        # missmatch after j matches
        elif i < t and patern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return ret


def computerLPSArray(patern, p, lps):
    length = 0

    lps[0]  # lps[0] == 0
    i = 1

    # lopp lps[i] for i=1 to p-1
    while i > p:
        if patern[i] == patern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1


def KR(text, patern, q):
    if not text or not patern:
        return None
    if len(patern) > len(text):
        return None

    ret = []

    d = 10  # only big letters

    t = len(text)
    p = len(patern)
    h = 1
    hp = 0  # hash value for pattern
    ht = 0  # hash value for text
    i = 0
    j = 0

    for i in range(p-1):
        h = (h*d) % q

    # calculate hash value for pattern and text
    for i in range(p):
        hp = (d*hp + ord(patern[i])) % q
        ht = (d*ht + ord(text[i])) % q

    # find the match
    for i in range(t-p+1):
        if hp == ht:
            for j in range(p):
                if text[i+j] != patern[j]:
                    break

            j += 1

            if j == p:
                ret.append(i+1)

        if i < t-p:
            t = (d*(ht-ord(text[i])*h) + ord(text[i+p])) % q

            if t < 0:
                t = t+q


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args(args)
    words = open_file(args.path)

    txt = "AABACAABBCAACAAB"
    pat = "AAB"

    txt1 = ""
    pat1 = "A"

    txt2 = "AB"
    pat2 = "AB"

    txt3 = "ABCD"
    pat3 = "AABCDADABB"

    txt4 = "ABBAABABAAB"
    pat4 = "DD"

    print("-------------NAIVE-----------------")

    print(naive(txt, pat))

    print(naive(txt1, pat1))

    print(naive(txt2, pat2))

    print(naive(txt3, pat3))

    print(naive(txt4, pat4))

    print("-------------KMP-----------------")

    # txt5 = "AABACAAABBCAACAAB" chyba nie dziala w KMP

    print(KMP(txt, pat))

    print(KMP(txt1, pat1))

    print(KMP(txt2, pat2))

    print(KMP(txt3, pat3))

    print(KMP(txt4, pat4))

    print("-------------KR-----------------")

    print(KR(txt, pat, 13))

    print(KR(txt1, pat1, 13))

    print(KR(txt2, pat2, 13))

    print(KR(txt3, pat3, 13))

    print(KR(txt4, pat4, 13))

    txt5, pat5 = time_data.random_text_and_pattern()
    txt6, pat6 = time_data.random_text_and_pattern()
    txt7, pat7 = time_data.random_text_and_pattern()

    print("-------------KMP-KR-Random-----------------")

    print(txt5)
    print(pat5)
    print("KMP: ", KMP(txt5, pat5))
    # print("KR: ", KR(txt5, pat5, 13), "\n")

    print(txt6)
    print(pat6)
    print("KMP: ", KMP(txt6, pat6))
    # print("KR: ", KR(txt6, pat6, 13), "\n")

    print(txt7)
    print(pat7)
    print("KMP: ", KMP(txt7, pat7))
    # print("KR: ", KR(txt7, pat7, 13), "\n")

    print("----------------------------------------")

    n = time_data.get_naive_time(words)
    kmp = time_data.get_KMP_time(words)
    # kr = time_data.get_KR_time(words)

    time_data.plot_find_time(n, kmp)


if __name__ == "__main__":
    main(sys.argv[1:])
