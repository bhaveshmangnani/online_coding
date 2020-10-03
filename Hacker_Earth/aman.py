d=int(input())
t=0
for i in range(d):
    r,x=input().split()
    if int(x)*100 == (2*22*int(r))/7:
        t+=1
print(t)