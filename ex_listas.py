

def remove_duplicates(l):
    l2 = list()
    for i in l:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2


if __name__ == '__main__':
    l1 = ['hello', 0, 23, 23, 23, 23, 'Osmar']
    result = remove_duplicates(l1)
    if len(result) < len(l1):
        print("We found duplicates!")
    else:
        print("No duplicates found!")