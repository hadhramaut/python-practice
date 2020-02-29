"""https://www.codewars.com/kata/secret-message/train/python"""


def find_secret_message(paragraph):
    paragraph = ''.join([c for c in paragraph.lower() if c in 'abcdefghijklmnopqrstuvwxyz '])
    temp, result = [], []
    for word in paragraph.split():
        if word not in temp:
            temp.append(word)
        elif word not in result:
            result.append(word)
    return " ".join(i for i in result)
