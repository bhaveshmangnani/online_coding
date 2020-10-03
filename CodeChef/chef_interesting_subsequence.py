def subs(t,n,k,ar):
    for _ in range(t):
        
        #n,k = [int(x) for x in input().split()]
        #ar = [int(x) for x in input().split()]
        
        ar.sort()
        print("ar=",ar)
        smain=sum(ar[:k+1])
        c=1
        ts=smain
        for i in range(n-k):
            ts=ts-ar[i]+ar[k+i]
            if ts != smain:
                break
            c+=1
        
        
        print(c)

import random

for i in range(5):
    n=random.randint(1,50)
    k=random.randint(1,n)
    lst=[]
    for i in range(n):
        lst.append(random.randint(1,100))
    print(f"n={n} k={k}\nlst={lst}")
    subs(1, n, k, lst)
    print("-----------------------------------------------")
