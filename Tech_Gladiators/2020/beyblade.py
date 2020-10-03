
def beyblade(t, n, gteam, oppo):
    
    for _ in range(t):

        #n=int(input())
        #gteam=[int(x) for x in input().split()]
        #oppo=[int(x) for x in input().split()]
        gteam.sort()
        oppo.sort()
        print(f"gt={gteam}\nop={oppo}")
        c=0
        gti=0
        for i in range(n):
            if gteam[i]>oppo[0]:
                #print("in")
                break
            gti+=1
        print(gti)
        oti=0
        while gti<n and oti<n:

            if gteam[gti]>oppo[oti]:
                c+=1
                oti+=1
            gti+=1

        #print(c)
        print("ANS=",c)
        

import random
t=random.randint(1,20)
for i in range(t):
    n=random.randint(1,10)
    lst=[]
    lst2=[]
    for i in range(n):
        lst.append(random.randint(1,100))
        lst2.append(random.randint(50,200))
    print(f"n={n} \ngteam={lst}\n oppo={lst2}")
    beyblade(1,n, lst, lst2)
    print("------------------------------------------------")
    
