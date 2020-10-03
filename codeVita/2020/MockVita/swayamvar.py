from collections import Counter
n = int(input())
bride = list(input())
groom = list(input())
dctg = dict(Counter(groom))


total = n
for i in range(n):
    if bride[i] in dctg and dctg[bride[i]]>0:
        total = total -1
        dctg[bride[i]]-=1
    else:
        break
print(total)
