def bf(n, k ,a):
    c=0
    s=0
    for i in range(n):
        tc=0
        ts=0
        for j in range(i,n):
            if (ts+a[j])%k!=0:
                print(f"j={j} a[j]={a[j]} ts={ts}")
                ts=ts+a[j]
                tc+=1
        if tc>c:
            c=tc
    print(c)
n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
bf(n,k,a)
