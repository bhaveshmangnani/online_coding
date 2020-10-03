
def o_n(t,n,a):
    

    for _ in range(t):
        
        #n=int(input())
        #a=[int(x) for x in input().split()]
        c=0
        l,r=-1,0
        i=0
        
        while i<n:
            if a[i]%4==0:
                #print(i)
                l=-1
                r=0
                i+=1
                continue
            elif a[i]%2==0 :
                break
            r+=1
            i+=1
        l=r
        r=0
        #print(i)
        i+=1
        if i<=n:
        
            while i<n:
                #print("iwe")
                
                if a[i]%4==0:
                    #print(i)
                    
                    c+=l+r+1+l*r
                    #print(l,r)
                    #print(c)
                    l=-1
                    r=0
                
                elif a[i]%2==0:
                    
                    
                    if l>=0:
                        #print(l,r)
                        c+=1+r+l+(l*r)
                        #print(i,c)
                    l=r
                    r=0
                else:
                    r+=1
                i+=1
            if l>=0:
                #print(l,r)
                c+=l+r+1+(l*r)
        print("o_n=",-c+(n*(n+1)//2))


def o_n2(t,n,a):
    
    for _ in range(t):
        
        #n=int(input())
        #a=[int(x) for x in input().split()]
        c=0
        
        for i in range(n):
            
            p=1
            for j in range(i,n):
                p=p*a[j]
                if p&1:
                    c+=1
                elif not p%4:
                    c+=1
        print("o_n2",c)

import random

t=random.randint(1,10)
for i in range(t):
    n=random.randint(1,20)
    lst=[]
    for _ in range(n):
        lst.append(random.randint(-100,100))
    print(lst)
    o_n(1,n,lst)
    o_n2(1,n,lst)

