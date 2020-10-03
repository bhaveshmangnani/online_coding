n=int(input())
stepsh=input()

count=0
scount=0

for i in range(n):
    if stepsh[i]=='U':
        scount+=1
    else:
        scount-=1
    print(f"scount={scount}, count={count}")
    
    if scount==0:
        count+=1

print(count)
