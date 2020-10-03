a,b=[int(x) for x in input().split()]

for i in range(a,b+1):
    
    flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=False
            break

        print(f"i={i} j={j} flag={flag}")
    if i==1:
        flag=False
    if flag:
        print(f"ans={i}")
