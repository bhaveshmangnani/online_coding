n=int(input())
ol=[int(x) for x in input().split()]
m=int(input())
al=[int(x) for x in input().split()]
alt=[]
alt.extend(al)
al=al[::-1]
rank=[]
r=0
for i in range(n):
    if ol[i]==ol[i-1]:
        rank.append(r)
    else:
        r+=1
        rank.append(r)

ans={}
for i in range(m):
    pos=0
    for j in range(n):
        if al[i]==ol[j]:
            pos=j
            ans[al[i]]=rank[j]
            break
        elif al[i]>ol[j]:
            pos=j
            ans[al[i]]=rank[j]
            for k in range(j,n):
                rank[k]+=1
            break
    else:
        pos=n+1
        ans[al[i]]=rank[-1]+1
    ol=ol[:pos+1]+[al[i]]+ol[pos+1:]
    rank=rank[:pos+1]+[ans[al[i]]]+rank[pos+1:]
    n+=1
for i in alt:
    print(ans[i])
