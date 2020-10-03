t=int(input())

for _ in range(t):
    
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    flag=True
    
    for i in range(0,m,n):
        
        temp={}
        for j in range(n):
            temp[j+1]=0
        
        for j in range(i,n+i):
            temp[a[j]] += 1
            print(f"i={i} j={j}")
        
        for j in range(1,n+1):
            if temp[j]!=1:
                flag=False
                break
        
    if flag:
        print("YES")
    else:
        print("NO")
