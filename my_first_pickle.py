import pickle

from my_first_file import reading, recover_list


def save_pickle(ob):
    with open('my_first_serialized_python_obj', 'wb') as f:
        pickle.dump(ob, f)
    print('Saved!!!')


def load_pickle():
    with open('my_first_serialized_python_obj', 'rb') as f:
        ll = pickle.load(f)
    print('A soma da lista lida é {}'.format(sum(ll)))
    print('Lida!')


if __name__ == '__main__':
    # r = reading()
    # l = recover_list(r)
    # save_pickle(l)
    load_pickle()
