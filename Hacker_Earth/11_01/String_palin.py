n=int(input())

s=input()

for i in range(n):
    l,r=[int(x) for x in input().split()]
    l-=1
    r-=1
    
    sl=list(set(s[l:r+1]))
    print(sl)
    
    fs = True
    for t in sl:
        nt=s[l:r+1].count(t)
        print(f"nt={nt} t={t} fs={fs}")
        if fs and nt==1:
            fs=False
            continue
        if fs or nt%2!=0:
            print("Impossible")
            break
            
    else:
        print("Possible")
        
