n,q=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
lsts=lst.copy()

for i in range(1,n):
    lsts[i]=lst[i]+lsts[i-1]
    
    

for i in range(q):
    start,end=[int(x) for x in input().split()]
    start=start-1
    end=end-1
    print(f"start={start},end={end} ")
    print(f"lst={lsts[start]},{lsts[end]} ")
    mean=lsts[end]-lsts[start]+lst[start]
    print(f"mean={mean}")
    mean=mean//(end-start+1)
    print(mean)
