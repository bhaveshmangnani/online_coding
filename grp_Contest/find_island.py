
r,c=[int(x) for x in input().split()]
a=0
for i in range(r):
    
    t="".join(input().split())
    t="0b"+t
    a=a|int(t,2)
print(bin(a).count("1"))
