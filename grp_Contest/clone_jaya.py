def GetLastNumber(L):
	i=len(L)-1
	while(i>=0 and L[i]==-1):
		i=i-1
	return i
L=[int(i) for i in input().split()]
space_count=0
for i in L:
	if i%2==0:
		space_count+=1
for i in range(space_count):
	L.append(-1)
#print(L)
def CloneEvenNumbers(L):
	if len(L)==0:
		print(-1)
		return
	i=GetLastNumber(L)
	end=len(L)
	while i>=0:
		if L[i]%2==0:
			end=end-1
			L[end]=L[i]
			end=end-1
			L[end]=L[i]
		else:
			end=end-1
			L[end]=L[i]
		i=i-1
CloneEvenNumbers(L)
print(L)

from array import *
n=int(input())
a=array("i",[int(x) for x in input().split()])
if n>0:
    for i in range(n):

        if not a[i]&1:
            print(a[i], end=" ")
        print(a[i], end=" ")
else:
    print(-1)
