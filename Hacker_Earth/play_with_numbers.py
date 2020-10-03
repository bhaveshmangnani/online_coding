n,q=input().split()
n=int(n)
q=int(q)
ar1=[int(x) for x in input().split()]
for i in range(q):
    xi,yi=input().split()
    print(int((ar1[int(xi)-1]+ar1[int(yi)-1])/2))