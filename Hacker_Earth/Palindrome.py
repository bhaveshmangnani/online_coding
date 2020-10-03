n=int(input())

s=input()

for i in range(n):
    l,r=[int(x) for x in input().split()]
    l-=1
    r-=1
    print(f"l={l} r={r}")
    dct={}
    for t in range(l,r+1):
        
        if s[t] in dct:
            dct[s[t]]+=1
        else:
            dct[s[t]]=1
        
    print(dct)
    flag=True
    fs=True
    
    
    for t in range(l,r+1):
       
        c=dct[s[t]]

        if c==1 and fs:
            fs=False
            continue
        
        if c%2!=0:
            flag=False
            break
            
        
    if flag:
        print("Possible")
    else:
        print("Impossible")
