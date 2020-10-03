n=int(input())
a=[int(x) for x in input().split()]

for i in range(n):
    pos=0
    for j in range(n):
        if a[j]==i-1:
            pos=j
            print(f"j={j},a[j]={a[j]},i={i}")
            break
    
    print(a[pos])
