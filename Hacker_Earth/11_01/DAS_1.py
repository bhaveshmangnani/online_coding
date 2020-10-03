def custom(ele):
    return ele[0]




n=int(input())
lst=[]
for i in range(n):
    lst.append([int(x) for x in input().split()])
    
    
    
lst.sort(key=custom)


c=n
for i in range(1,n):

    for j in range(n):
        if lst[i][0]>lst[j][1]:
            c-=1
            break

    
    
print(c)
