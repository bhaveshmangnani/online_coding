a=[int(x) for x in input().split()]
k=int(input())

ta=[x+k for x in a]
print(ta)

la=len(a)

for i in range(la):

    for j in range(i+1,la):
        print(f"i={i}, j={j}, d={a[i]-a[j]}")
