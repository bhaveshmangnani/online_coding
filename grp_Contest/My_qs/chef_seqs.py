for _ in range(int(input())):
        
    n,k = [int(x) for x in input().split()]
    ar = [int(x) for x in input().split()]
    ar.sort()

    le=ar[k-1]
    lec=0
    lec_in_k=0
    for i in range(k-1,-1,-1):
        if ar[i]!=le:
            break
        lec+=1

    lec_in_k=lec
    for i in range(k,n):
        if ar[i]!=le:
            break
        lec+=1

    import math
    n=math.factorial(lec)
    d=math.factorial(lec_in_k)*math.factorial(lec - lec_in_k)
    print(n//d)
