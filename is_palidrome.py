""" Exemplo de construção de palíndrome
    Exercício de lista e índices
    """


def first_letter(word):
    return word[0]


def last_letter(word):
    return word[-1]


def middle_word(word):
    return word[1:-1]


def main(word):
    if len(word) < 2:
        return True
    if first_letter(word) != last_letter(word):
        return False
    else:
        return main(middle_word(word))


if __name__ == '__main__':
    w = 'tattarrattat'
    # print(first_letter(w))
    # print(last_letter(w))
    # print(middle_word(w))
    print(main(w))
