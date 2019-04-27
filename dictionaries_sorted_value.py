""" Sort dictionaries by value
"""


def sort_by_value(d):
    return sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)


if __name__ == '__main__':
    d = {'a': 0, 'b': 1, 'c': 14, 'd': 12}
    print(sort_by_value(d))
