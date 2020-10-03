m,n=[int(x) for x in input().split()]
t=m*n
ans=0
if m==1 or n==1:
    ans=t//2
else:
    tm=m//2
    tn=n//2
    rm=m-2*tm
    rn=n-2*tn
    
    ans=tm*tn
    ans=ans+((rm*n)//2)+((rn*m)//2)

print(ans)
