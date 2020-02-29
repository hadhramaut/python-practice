"""https://www.codewars.com/kata/permutations"""

import itertools


def permutations(string):
    return ["".join(item) for item in list(set(itertools.permutations(string)))]