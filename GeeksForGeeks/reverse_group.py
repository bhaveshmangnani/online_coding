#code
def rev(t,n , k,arr):
    #for _ in range(int(input())):
    for _ in range(t):    
        #n,k = [int(x) for x in input().split()]
        #arr = [int(x) for x in input().split()]
        arr2 = arr.copy()
        
        for i in range(0,n,k):
            start = i
            end = min(i + k,n)-1
            #print(f"s={start} e={end}")
            for j in range( (end-start+1)//2 ):
                jth = arr[start+j]
                kth = arr[end - j]
                #print(f"j={jth} k={kth}")
                arr[start +j]=kth
                arr[end-j]=jth

        #print("sc = ",end="")
        tans=[]
        for i in range(0,n,k):
            start=i
            end = min(i+k,n)
            tans.extend(arr2[start:end][::-1])
            #print(*arr2[start:end][::-1],end=" ")
        #print()
            
        
        #print("my = ",end="")       
        #print(*arr)
        if arr!=tans:
            print(f"act ={tans}\nmy={arr}")

import random
t = random.randint(2,10)
print(t)
for _ in range(t):
    n = random.randint(2,10)
    lst = []
    for _ in range(n):
        lst.append(random.randint(1,20))
    k = random.randint(1,n)
    print(n,k)
    print(*lst)
    rev(1,n,k,lst)
    print("=="*15)
    
            
            
    

