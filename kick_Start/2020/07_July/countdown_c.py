
for case in range(int(input())):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    c=0
    i=0
    while i<n-k+1:
        if a[i]==k:
            j=i+1
            f=True
            while j<i+k:
                if a[j-1]!=a[j]+1:
                    i=j
                    f=False
                    break
                j+=1
            if f:
                i=i+k
                c+=1
        i+=1
    
    
    print("Case #{}: {}".format(case+1,c))
