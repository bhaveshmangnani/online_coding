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
ai=0
ni=n-1

while ab[ai]<sb[-1]:
    ar.append(rb[-1]+1)
    ai+=1

print(ar)
while ai<m:
    while ab[ai]>=sb[ni] and ni>=0:
        ni-=1
    ar.append(rb[ni+1])
    ai+=1

for i in ar:
    print(i)
