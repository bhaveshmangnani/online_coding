def solve(nk,t):
    for t_itr in range(t):
        #nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        max=0
        f=False
        for i in range(1,n+1):

            for j in range(i+1,n+1):
                t=i&j
                if t>=k:
                    f=True
                    break
                if t>max:
                    max=t
            if f:
                break
        print(max)
import random
t=random.randint(5,15)
for i in range(t):
    n=random.randint(2,100)
    k=random.randint(2,n)
    print(n,k)
    solve([n,k],1)
