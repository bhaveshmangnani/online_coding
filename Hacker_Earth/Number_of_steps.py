n=int(input())
a=[int(x) for x in input().split()]

b=[int(x) for x in input().split()]
step=0
mnum=min(a)
mnum=5
for i in range(n):
    
    if a[i]>mnum and a[i]>=b[i]:
        if b[i]==0:
            step=0
            break
        step=step+(a[i]-mnum)//b[i]
    
if not step:
    print(-1)
else:
    print(step)
