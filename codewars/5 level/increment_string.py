"""https://www.codewars.com/kata/string-incrementer"""


def increment_string(string):
    head = string.rstrip("0123456789")
    tail = string[len(head):]
    if not tail:
        return string + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
