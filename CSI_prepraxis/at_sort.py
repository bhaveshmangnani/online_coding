def custom(ele):
    return ele[k]




n,m=[int(x) for x in input().split()]

lst=[]
for i in range(n):
    lst.append([int(x) for x in input().split()])
    
k=int(input())
lst.sort(key=custom)
print(lst)
