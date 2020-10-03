
def solve(r,c,grid):
    temp=[]
    for _ in range(r):
        temp.append(list("O"*c))
    for i in range(r):

        for j in range(c):

            if grid[i][j]=="O":
                temp[i][j]="."
                if i-1>-1:
                    temp[i-1][j]="."
                if i+1<r:
                    temp[i+1][j]="."
                if j>0:
                    temp[i][j-1]="."
                if j<c-1:
                    temp[i][j+1]="."
    return temp
    


r,c,t=[int(x) for x in input().split()]
if t%2:
    grid=[]
    for _ in range(r):
        grid.append(list(input()))
    grid = solve(r,c,grid)
    if t%4==1:
        grid = solve(r,c,grid)
    for i in grid:
        print("".join(i))
    
else:
    for _ in range(r1):
        print("O"*c1)
