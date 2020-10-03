
for case in range(int(input())):
    
    n= int(input())
    lst=[]
    r=0
    for i in range(n):
        tl=[int(x) for x in input().split()]
        lst.append(tl)
        f=False
        for j in range(n):
            for k in range(j+1,n):
                if tl[j]==tl[k]:
                    r+=1
                    f=True
                    break
            if f:
                break
        
    t=lst[0][0]
    
    for i in range(1,n):
        t+=lst[i][i]
    cd=0
    
    for c in range(n):
        cflag=False
        for ci in range(n):
            
            for cr in range(ci+1,n):
                if lst[ci][c]==lst[cr][c]:
                    cd+=1
                    cflag=True
                    break
            if cflag:
                break
        
    print(f"Case#{case}: {t} {r} {cd}")        
                
