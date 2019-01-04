# Sin terminar

from math import sqrt
from collections import defaultdict


class Node():
    def __init__(self, val):
        self.value = 1


class Tree():

    def __init__(self):
        self.vecinos = defaultdict(lambda x: set([]))

    def add_edge(self, u, v, val, prob):
        self.vertices[u].add((v, val, prob))


def get_dividers(num):
    divs = []
    for i in range(1, int(sqrt(num)+1)):

        if num % i == 0:
            if num / i == i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(num // i)
    divs.sort()
    return divs


def get_subdividers(num, ls):
    subdivs = []
    for i in ls:
        if i <= num and num % i == 0:
            subdivs.append(i)
        elif i > num:
            break
    return subdivs


n, k = list(map(int, input().split()))
dividers = get_dividers(n)
expected_value = {div: 0 for div in dividers}
dict_dividers = {div: get_subdividers(div, dividers) for div in dividers}


