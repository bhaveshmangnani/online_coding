def eff(n,k,a):
    from collections import Counter
    #n,k=[int(x) for x in input().split()]
    #a=[int(x)%k for x in input().split()]
    a=[x%k for x in a]
    dct=dict(Counter(a))

    for i in range(k):
        if i not in dct:
            dct[i]=0
    i=0
    j=k-1
    c=0
    while i<=j:
        c=c+min(k-1, max(dct[i], dct[j]))
        i+=1
        j-=1
    print(c)

def bf(n,k,a):

    c=0
    s=0
    for i in range(n):
        tc=0
        ts=0
        for j in range(i,n):
            if (ts+a[j])%k==0:
                ts=ts+a[j]
                tc+=1
        if tc>c:
            c=tc
    print(c)

import random


n=random.randint(5,20)
k=random.randint(1,100)
lst=[]

for i in range(n):
    lst.append(random.randint(1,500))

print(f"n={n} k={k}\nlst={lst}")
eff(n,k,lst)
bf(n,k,lst)

