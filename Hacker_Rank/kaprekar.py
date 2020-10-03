
p=int(input())
q=int(input())
lst=[]
for i in range(1,10000000):
    s=i**2
    ss=str(s)
    ls=len(ss)
    lls=ls//2
    l=ss[0:lls]
    r=ss[lls:]
    #l=ss[rs+1:]
    #print(f"rs={lls}")
    #print(f"r={r} l={l}")
    if not l:
        l=0
    if not r:
        r=0
    if int(l)+int(r)==i:
        lst.append(i)
        #print(i)
print(lst)
