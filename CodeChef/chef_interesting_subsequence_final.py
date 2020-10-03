def subs_main(t,n,k,ar):
    for _ in range(t):
        
        #n,k = [int(x) for x in input().split()]
        #ar = [int(x) for x in input().split()]
        ar.sort()
        
        le=ar[k-1]
        lec=0
        lec_in_k=0
        for i in range(k-1,-1,-1):
            if ar[i]!=le:
                break
            lec+=1
            
        lec_in_k=lec
        for i in range(k,n):
            if ar[i]!=le:
                break
            lec+=1
            
        import math
        n=math.factorial(lec)
        d=math.factorial(lec_in_k)*math.factorial(lec - lec_in_k)
        print("ans=",n//d)

import random
t=random.randint(3,10)
print(t)
for i in range(t):
    n=random.randint(49,50)
    k=random.randint(1,n)
    print(n,k)
    lst=[]
    for i in range(n):
        nn=random.randint(20,30)
        print(nn,end=" ")
        lst.append(n)
    #print(f"n={n} k={k}\nlst={lst}")
    print()
    subs_main(1, n, k, lst)
    print("-----------------------------------------------")
