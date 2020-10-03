m,n=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

count=0

a.sort()
b.sort()
mnum=b[0]
flag=True

for i in range(2,mnum+1):
    flag=True
    for j in range(m):
        if i%a[j] !=0:
            flag=False
            break
    if flag :
        for k in range(n):
            if b[k]%i !=0:
                flag=False
                break
    
    if flag:
        count+=1

print(count)
