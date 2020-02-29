"""https://www.codewars.com/kata/sum-of-pairs"""


def get_sums(lst, target):
    already_seen = set()
    pairs = []
    for x in lst:
        if (target - x) in already_seen:
            pairs.append((x, target - x))
        already_seen.add(x)
    return list(reversed(pairs))


print(get_sums([1, 4, 8, 7, 3, 15], 8))
print(get_sums([1, -2, 3, 0, -6, 1], -6))
print(get_sums([10, 5, 2, 3, 7, 5], 10))
print(get_sums([20, -13, 40], -7))
a = [x for x in range(100000)]
print(get_sums(a, a[-1] + a[-2]))
print(get_sums([1, 4, 8, 7, 3, 15], 8))