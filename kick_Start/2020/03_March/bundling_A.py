
for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    sl=[]
    for _ in range(n):
        sl.append(input())
    
    sl.sort()
    s=0
    for j in range(0,k,n):
        cmn=0
        for k in range(len(sl[j])):
            if sl[j][k]!=sl[j+1][k]:
                break
            else:
                cmn+=1
        s+=cmn
    print("Case #"+str(i+1)+":",s)
