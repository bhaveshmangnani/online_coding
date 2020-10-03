def climb(n,sb,m,ab):
    #n=int(input())
    #sb=[int(x) for x in input().split()]
    #m=int(input())
    #ab=[int(x) for x in input().split()]

    rb=[]
    rb.append(1)
    r=1
    for i in range(1,n):
        
        if sb[i]<sb[i-1]:
            r+=1
        rb.append(r)

    ar=[]
    ai=0
    ni=n-1

    while ab[ai]<sb[-1]:
        ar.append(rb[-1]+1)
        ai+=1

    while ai<m:
        while ni>0 and ab[ai]>=sb[ni] :
            ni-=1
        if ab[ai]>=sb[ni]:
            ar.append(rb[ni])
        else:
            ar.append(rb[ni+1])
        ai+=1

    for i in ar:
        pass
        print(i,end=" ")

def climb2(n,sb,m,ab):
    #n=int(input())
    #sb=[int(x) for x in input().split()]
    #m=int(input())
    #ab=[int(x) for x in input().split()]
    sb=list(set(sb))
    sb.sort(reverse=True)
    ai=0
    ni=len(sb)-1
    while ai<m:
        if ab[ai]>=sb[ni]:
            break
        print(ni+2,end=" ")
        ai+=1

    #print(sb)
    while ai<m:
        while ni>0 and sb[ni]<ab[ai]:
            #print("ai=",ai,"ni=",ni)
            ni-=1
        #print("ai=",ai,"ni=",ni,"abi=",ab[ai],"sbi=",sb[ni])
        if sb[ni]>ab[ai]:
            print(ni+2,end=" ")
        elif sb[ni]==ab[ai]:
            print(ni+1,end=" ")
        else:
            print(1,end=" ")
        ai+=1


import random as rn
t=5
for i in range(t):
    n=rn.randint(1,20)
    sb=[]
    for j in range(n):
        sb.append(rn.randint(0,200))
    sb.sort(reverse=True)
    k=rn.randint(5,20)
    ab=[]
    for j in range(k):
        ab.append(rn.randint(0,200))
    ab.sort()
    print(f"n={n}\nsb={sb}\nk={k}\nab={ab}")
    #n=int(input())
    #sb=[int(x) for x in input().split()]
    #m=int(input())
    #ab=[int(x) for x in input().split()]
    print("prev\tnew")
    climb(n,sb,k,ab)
    print()
    climb2(n,sb,k,ab)
    print()
    print("--------------------------------------------------------------------")
    
