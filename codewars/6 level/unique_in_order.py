# https://www.codewars.com/kata/54e6533c92449cc251001667


def unique_in_order(iterable):
    ls, prev = [], ''
    for char in iterable:
        if char != prev:
            ls.append(char)
            prev = char
    return ls
