lst = [int(x) for x in input().split()]

lst.sort(reverse=True)
max1 = lst[0]
max2 = lst[1]
print("\n",lst)

for t in lst[2:]:
    print(f"t={t} 1={max1} 2={max2}")
    if max1+t>max2+t:
        max2+=t
    else:
        max1+=t
print(max(max1,max2))
