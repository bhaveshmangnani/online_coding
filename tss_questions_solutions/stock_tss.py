arr = [90, 30, 20, 50, 40, 10, 70, 75, 5 ]
buy=arr[0]
sell=arr[0]
maxd=0
n=len(arr)

smin=arr[0]
smax=arr[0]
tempmin=arr[0]
for i in range(n):
	if arr[i]<tempmin:
		tempmin=arr[i]
	else:
		smin=tempmin
		smax=arr[i]
print("buy=",smin,"sell=",smax)



	