
ss=set()
for i in range(100000):
    ss.add(i**2)

for case in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    c=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=a[j]
            #sqt=math.sqrt(s)
            if s in ss:
                c+=1
    print("Case #{}: {}".format(case+1,c))
