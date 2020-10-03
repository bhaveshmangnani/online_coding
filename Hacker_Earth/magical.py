n=int(input())

plist=[67, 71, 73, 79, 83, 89,97, 101, 103, 107, 109, 113]


        
        
for i in range(n):
    answer=""
    t=int(input())
    word=input()
    
    for k in word:
        asci=ord(k)
        diff=plist[0]-asci
        
        for z in plist:
            print(f"diff for {k} = {diff}   asci={asci+diff}")
            if abs(asci-z)<abs(diff):
                diff=z-asci
            
        answer+=chr(asci+diff)
    print(answer)
