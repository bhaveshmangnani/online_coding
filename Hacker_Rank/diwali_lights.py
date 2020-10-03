import math
def ncr(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

def lights1(n):
    s=0
    for i in range(1,n+1):
        s=s+ncr(n,i)
    return s

def lights(n):
    if n==1:
        return 1
    if n==2:
        return 3

    prev=n
    c=n
    s=2*n
    if n%2==0:
        for i in range(1,n//2-1):
            prev=c
            c=c*(n-i)//(i+1)
            #print(c)
            s=s+2*c
        c=c*(n-n//2+1)//(n-n//2)
        #print(c)
        s=s+c
    else:
        for i in range(1,n//2):
            prev=c
            c=c*(n-i)//(i+1)
            s=s+2*c
        
    return s+1

for _ in range(int(input())):
    for t in range(1,20):
        print("-"*20)
        print(t)
        bf=lights1(t)
        ef=lights(t)
        print("bf=",bf)
        print("ef=",ef)
        if bf-ef:
            print("WA".center("*",10))
        
