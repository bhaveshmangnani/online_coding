

t=int(input())

for i in range(t):

    n=int(input())

    
    
    lst=[int(x) for x in input().split()]
    first=max(lst)
    second=None

    summax=first
    print(n)
    for j in range(n-1,-1,-1):

        for k in range(j-2,-1,-1):
            print("first=",first,"second=",second,"\n","j=",j,"k=",k)
            print("sum=",summax)
            if lst[j]+lst[k]>summax:
                first=lst[j]
                second=lst[k]
                summax=lst[j]+lst[k]
                continue
            if lst[j]+lst[k]==summax:
                if lst[j]>first:
                    first=lst[j]
                    second=lst[k]
                    summax=first+second
                    continue

    if second:
        print(first,second,sep='')
    else:
        print(first)

