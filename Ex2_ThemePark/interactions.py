from Ex2_ThemePark.account import Agent, Shop
import random


def creation(f, i, n, p):
    l = list()
    for i in range(i, n):
        l.append(f(i, p))
    return l


def interact(a, s):
    for i in range(len(a)):
        s1 = random.choice(s)
        if a[i].check_funds(s1):
            if s1.visit():
                s1.account.deposit(a[i].account.pay(s1.cost))
                a[i].get_fun(s1.fun)


def salaries(a, p):
    for i in range(len(a)):
        a[i].account.deposit(random.randrange(p['salaries'][0], p['salaries'][1]))


def averaging(a, s):
    avg_fun = sum([i.fun for i in a]) / len(a)
    avg_shop_balance = sum([i.account.balance for i in s]) / len(s)
    avg_consumer_balance = sum([i.account.balance for i in a]) / (len(a))
    # print('Average fun for this configuration is {:.2f}'.format(avg_fun))
    # print('Average shop balance for this configuration is {:.2f}'.format(avg_shop_balance))
    # print('Average consumer balance for this configuration is {:.2f}'.format(avg_consumer_balance))
    # print("")
    # print("----------------------------------")
    return avg_fun, avg_shop_balance, avg_consumer_balance


def main(n1, n2, p):
    agents = creation(Agent, 0, n1, None)
    shops = creation(Shop, n1, n1 + n2, p)
    random.shuffle(agents)
    random.shuffle(shops)
    salaries(agents, p)
    interact(agents, shops)

    return averaging(agents, shops)


if __name__ == '__main__':
    a = 10
    s = 20
    f, sb, cb = main(a, s)
