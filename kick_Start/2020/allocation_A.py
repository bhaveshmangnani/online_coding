
for i in range(int(input())):
    n,b=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a.sort()
    cst=0
    c=0
    for j in range(n):
        if cst+a[j]>b:
            break
        else:
            c+=1
            cst+=a[j]
    print(f"Case #{i+1}: {c}")
