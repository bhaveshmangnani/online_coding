n=int(input())
sb=[int(x) for x in input().split()]
m=int(input())
ab=[int(x) for x in input().split()]

rb=[]
rb.append(1)
r=1
for i in range(1,n):
    
    if sb[i]<sb[i-1]:
        r+=1
    rb.append(r)

ar=[]

a=0
ni=n-1
ait=0

if ab[a]<sb[-1]:
    print(rb[-1]+1)
    ait+=1
    a+=1

while ait<m and ni>-1:

    if ab[a]<sb[ni]:
        print(rb[ni]+1)
        ait+=1
        a+=1
    elif ab[a]==sb[ni]:
        print(rb[ni])
        ait+=1
        a+=1
    ni-=1
for i in range(m-ait):
    print(1)

