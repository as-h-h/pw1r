# Zliczanie sĹĂłw, c.d.
# Wszystkie* warianty funkcji do zliczania sĹĂłw/liter z wykĹadu zebrane w jeden plik.
# * PominiÄty zostaĹ wariant "rÄcznej" konstrukcji sĹownika odpowiadajÄcego Counter.
# Wszystkie uĹźywane pliki tekstowe sÄ w materiaĹach do WykĹadu 6.

import string
import numpy as np
import matplotlib.pyplot as plt
import string
from collections import Counter


def word_counts(input_file):
    d = Counter()
    with open(input_file, encoding='utf8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.strip(string.punctuation).casefold()
                if word == "":
                    continue
                d.update([word])
    return d


def letter_counts(input_file):
    d = Counter()
    with open(input_file, encoding='utf8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.strip(string.punctuation).casefold()
                if word == "":
                    continue
                d.update(word)  # word to ciÄg znakĂłw
    return d


'''
def print_top_words_00(input_file, num=10):  # pierwsza, bardziej prymitywna wersja
    d = word_counts(input_file)
    lst = [(count, word) for word, count in d.items()]
    lst.sort(reverse=True)
    print(f"Top {num} sĹĂłw w pliku {input_file}:")
    for count, word in lst[:num]:
        print(f"{word:20} : {count}")


def print_top_words_01(input_file, num=10):  # druga wersja, korzystajÄca z klucza sortowania
    d = word_counts(input_file)
    lst = sorted(d, key=d.get, reverse=True)[:num]
    print(f"Top {num} sĹĂłw w pliku {input_file}:")
    for word in lst:
        print(f"{word:20} : {d[word]}")
'''


def print_top_words(input_file, num=10):  # wersja korzystajÄca wprost z Counter.most_common
    d = word_counts(input_file)
    lst = d.most_common(num)
    print(f"Top {num} sĹĂłw w pliku {input_file}:")
    for word, count in lst:
        print(f"{word:20} : {count}")


def print_top_letters(input_file, num=10):
    d = letter_counts(input_file)
    lst = d.most_common()
    print(f"Top {num} liter w pliku {input_file}:")
    for letter, count in lst[:num]:
        print(f"{letter:3} : {count}")


def list_words_in_file(input_file):
    lst = []
    with open(input_file, encoding='utf8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.strip(string.punctuation).casefold()
                if word == "":
                    continue
                lst.append(word)
    return lst


def draw_top_words(input_file, num=10):
    lst = list_words_in_file(input_file)
    words, counts = np.unique(lst, return_counts=True)
    idx = np.argsort(counts)[:-(num+1):-1]
    plt.title(f"Top {num} sĹĂłw w pliku {input_file}:")
    xs, ys = [], []
    for i in idx:
        xs.append(words[i])
        ys.append(counts[i])
    plt.bar(xs, ys)
    plt.show()


###############
def draw_freq_words_plot(input_file, num=10):
    lst = list_words_in_file(input_file)
    words, counts = np.unique(lst, return_counts=True)
    idx = np.argsort(counts)[:-(num+1):-1]
    plt.title(f"Częstotliwość n-tego słowa")
    xs, ys = [], []
    for i in idx:
        xs.append(words[i])
        ys.append(counts[i]/counts.sum())
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(xs, ys)
    plt.show()

############


def draw_words_hist(input_file):
    d = word_counts(input_file)
    lst = [len(word) for word in d]
    plt.title(f"DĹugoĹci (unikalnych) sĹĂłw w pliku {input_file}")
    plt.hist(lst, bins=range(min(lst), max(lst) + 2))
    plt.show()


def draw_words_nonunique_hist(input_file):
    lst = [len(word) for word in list_words_in_file(input_file)]
    plt.title(f"DĹugoĹci sĹĂłw w pliku {input_file}")
    plt.hist(lst, bins=range(min(lst), max(lst) + 2))
    plt.show()


#if __name__ == "__main__":
    # print_top_words_00("20000en.txt", 10)
    # print_top_words_01("20000en.txt", 10)
    # print_top_words("20000en.txt", 10)
    # print_top_words("southpole.txt", 10)
    # print_top_letters("politeia.txt", 5)
    # draw_top_words("20000.txt", 10)
    # draw_words_hist("prideandprejudice.txt")
    # draw_words_nonunique_hist("prideandprejudice.txt")
    