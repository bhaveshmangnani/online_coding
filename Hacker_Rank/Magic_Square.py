a=[]
for _ in range(3):
    t=[int(x) for x in input().split()]
    a.extend(t)
a.sort()
dlen=0
dl=[]
for i in range(1,9):
    if a[i-1]==a[i]:
        dl.append(a[i])
        dlen+=1
c=0
nl=[]
aset=set(a)
nl=sorted(list(set(range(1,10))-aset))
for i in range(dlen):
    c+=abs(nl[i]-dl[i])
print(c)
