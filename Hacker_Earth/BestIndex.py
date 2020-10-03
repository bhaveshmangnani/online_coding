n=int(input())

mlst=[int(x) for x in input().split()]

lst=[]
start=1
step=2

for i in range(1,n+1):
    #to make the patter of 1,1,3,3,3,6,6,6,6,10,10,10,10
    final=start
    if final +step<=i:
        final+=step
        start=final
        step+=1
    lst.append(final)

lst=lst[::-1]

slst=[]
slst.append(mlst[0])

for i in range(1, n):
    #lst of sums of terms till i
    slst.append(slst[-1]+mlst[i])
    

msum=-11111111111111111111111111111111111111111111111111111111111111111111111111111111
 
for i in range(n):
    #final sum and check
    s=slst[lst[i]+i-1]-slst[i]+mlst[i]
    print(f"i={i} lst[i]={lst[i]} slst[lst[i]+i-1] = {slst[lst[i]+i-1]} slst[i]={slst[i]}")
    print(f"mlst[i]={mlst[i]}")
    msum=max(s,msum)
print(msum)
