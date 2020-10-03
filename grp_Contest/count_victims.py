
for _ in range(int(input())):
    n=int(input())
    name=input().split()
    dctl=[]
    for i in range(n):
        t={}
        for j in list(set(name[i])):
            t[j]=name[i].count(j)
        dctl.append([t,True])
    ans=[]
    for i in range(n):
        if dctl[i][1]:
            dctl[i][1]=False
            c=1
            for j in range(i+1,n):
                if dctl[i][0]==dctl[j][0] and dctl[j][1]:
                    c+=1
                    dctl[j][1]=False
            ans.append(c)
    ans.sort()
    for i in ans:
        if i:
            print(i,end=" ")
    print()
        
    
