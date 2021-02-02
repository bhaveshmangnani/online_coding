#URL:https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

dct = OrderedDict()

for _ in range(int(input())):
    ip = input().split()
    name = " ".join(ip[:len(ip)-1])
    price = int(ip[-1])
    if name in dct:
        dct[name]+=price
    else:
        dct[name]=price

for k in dct:
    print(k,dct[k])
