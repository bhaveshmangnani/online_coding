




t=int(input())




for i in range(t):

    n=int(input())

    
    
    lst=[int(x) for x in input().split()]
    first=max(lst)
    second=0
    summax=first


    for j in range(n):


        tempfirst=lst[j]
        for k in range(j+2,n):
            tempsecond=lst[k]
            tempsum=tempfirst+tempsecond
            if tempsum>summax:
                first=tempfirst
                second=tempsecond
                summax=tempsum
                continue
            elif tempsum==summax:
                if first>tempfirst:
                    first=tempfirst
                    second=tempsecond
                    summax=tempsum

    if second!=0:
        print(second,first,sep='')
    else:
        print(first)
