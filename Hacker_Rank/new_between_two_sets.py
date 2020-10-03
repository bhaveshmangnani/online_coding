def gcd(a, b):  
    if a == 0 : 
        return b

    return gcd(b%a, a)


m,n=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

count=0

gcdn=gcd(b[0],b[1])

for i in range(2,n):
    
    gcdn=gcd(gcdn,b[i])
    

lcmn=a[0]*a[1]
lcmn//=gcd(a[0],a[1])

for i in range(2,m):
    t=lcmn
    lcmn=lcmn*a[i]
    lcmn=lcmn//gcd(t,a[i])

print(lcmn,gcdn,gcdn//lcmn)

for i in range(1,(gcdn//lcmn)+1):
    if gcdn%(lcmn*i)==0:
        count+=1

print(count)
