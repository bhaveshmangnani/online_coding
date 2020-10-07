arr=[90, 30, 20, 50, 40, 10, 70, 75, 5 ]
arr.sort()
maxd=0
buy=arr[0]
sell=arr[1]
n=len(arr)
for i in range(1,n):
	if arr[i]-arr[i-1]>maxd:
		maxd=arr[i]
		buy=arr[i-1]
		sell=arr[i]
print("buy=",buy,"sell=",sell)
		