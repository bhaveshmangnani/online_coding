def solve(nc,ns,space):
    #nc,ns=[int(x) for x in input().split()]
    #space=[int(x) for x in input().split()]

    if nc==ns:
        print(0)



    else:
        space.sort()
        m=max(space[0], nc-space[-1]-1)
        for i in range(1,ns):
            m=max(m, (space[i]-space[i-1])//2)
        
        print(m)
from random import randint as ri
t=ri(1,5)
for i in range(t):
    nc=ri(5,10)
    ns=ri(1,nc)
    lst=[]
    for j in range(ns):
        lst.append(ri(0,nc-1))
    print(f"for{i+1}".center(20,"-"))
    print(nc,ns)
    print(*sorted(lst))
    solve(nc, ns, lst)
