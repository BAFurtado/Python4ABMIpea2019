import json

from my_first_file import reading, recover_list


def save_json(ob):
    with open('my_obj.json', 'w') as f:
        json.dump(ob, f)
    print('Saved! You can check my_obj.json')


def load_json():
    with open("my_obj.json", "r") as f:
        ll = json.load(f)
    print('A soma da lista lida é {:,.0f}'.format(sum(ll)))


if __name__ == '__main__':
    r = reading()
    l = recover_list(r)
    save_json(l)
    load_json()

