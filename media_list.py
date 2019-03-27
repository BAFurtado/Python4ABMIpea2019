""" Function to calculate the average of a list of integers
"""

def media(l):
    return sum(l)/len(l)


if __name__ == '__main__':
    example = [6, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 4, 90]
    print('A média é {:.3f}'.format(media(example)))