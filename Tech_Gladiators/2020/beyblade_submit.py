
for _ in range(int(input())):

    n=int(input())
    gteam=[int(x) for x in input().split()]
    oppo=[int(x) for x in input().split()]
    gteam.sort()
    oppo.sort()
    #print(f"gt={gteam}\nop={oppo}")
    c=0
    gti=0
    for i in range(n):
        if gteam[i]>oppo[0]:
            #print("in")
            break
        gti+=1
    #print(gti)
    oti=0
    while gti<n and oti<n:

        if gteam[gti]>oppo[oti]:
            c+=1
            oti+=1
        gti+=1

    print(c)
    
    
