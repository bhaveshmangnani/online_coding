

for case in range(int(input())):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append( [int(x) for x in input().split()] )
    
    dct = {}
    for i in range(n):
        dct[i]=0
        dct[-i]=0
    
    for i in range(n):
        
        for j in range(n):
            dct[j-i]=dct[j-i]+grid[i][j]
    
    
    print("Case #{}: {}".format(case+1,max(list(dct.values()))))
