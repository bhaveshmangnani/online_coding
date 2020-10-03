#n,m=[int(x) for x in input().split()]
al=[]
import random
n = random.randint(3,7)
m = random.randint(3,7)
tl=[]
print("-------------------------------------")
print(f"n={n} m={m}")
for i in range(n):
    s=""
    for i in range(m):
        s=s+str(random.randint(0,1))
    tl.append(s)
    print(s)
    

for i in range(n):
    al.append(int(tl[i],2))
    
m=0
c=0
for i in range(n):


    for j in range(i+1,n):
        t=al[i]|al[j]
        if t>m:
            c=1
            m=t
        elif t==m:
            c+=1
tm=0
for i in bin(m)[2:]:
    if i=="1":
        tm+=1

print(tm,c,sep="\n")
