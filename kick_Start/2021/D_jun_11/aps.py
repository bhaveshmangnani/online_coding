

for i in range(int(input())):
    a1,b1,c1 = map(int, input().split())
    a2,c2 = map(int, input().split())
    a3,b3,c3 =map(int, input().split())
    grid = [ [a1,b1,c1], [a2,None, c2], [a3,b3,c3] ]
    
    freq = {}
    
    lst=[ [[0,0],[2,2]], [[0,1],[2,1]], [[0,2],[2,0]], [[1,0],[1,2]] ]
    for [x1,y1], [x2,y2] in lst:
        num = (grid[x1][y1]+grid[x2][y2])/2
        if num==int(num):
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
    aps = 0    
    if freq:
        aps = max(freq.values())
    if (grid[0][0]-grid[0][1]) == (grid[0][1]-grid[0][2]):
        
        aps+=1
    if (grid[0][0]-grid[1][0]) == (grid[1][0]-grid[2][0]):
        aps+=1        
    if (grid[2][0]-grid[2][1]) == (grid[2][1]-grid[2][2]):
        aps+=1
    
    if (grid[0][2]-grid[1][2]) == (grid[1][2]-grid[2][2]):
        aps+=1
    print(f"Case #{i+1}: {aps}")
