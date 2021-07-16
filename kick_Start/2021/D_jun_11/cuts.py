for case in range(int(input())):
    
    n,c = map(int,input().split())
    #intervals = []
    #possible_cuts = []
    length = 0
    dct = {}
    for j in range(n):
        interval =list(map(int,input().split()))
        #possible_cuts.extend()
        cuts = range(interval[0]+1,interval[1])
        for cut in cuts:
            if cut in dct:
                dct[cut]+=1
            else:
                dct[cut] = 1
                length +=1
        #intervals.append(interval)
    
    #length = 0
    #dct ={}
    
    cuts = sorted(dct, key = lambda ele: dct[ele], reverse = True)
    ans = n
    for i in range(min(c,length)):
        ans += dct[cuts[i]]
    print(f"Case #{case+1}: {ans}")
