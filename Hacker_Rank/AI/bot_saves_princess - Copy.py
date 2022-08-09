#URL: https://www.hackerrank.com/challenges/saveprincess2

def nextMove(n,r,c,grid, py):
    if py != r:
        return "UP" if r>py else "DOWN"
    px = -1
    for i in range(n):
        if grid[py][i] == 'p':
            px = i
            break
    return "LEFT" if c>px else "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]

grid = []
py = -1
found = False

for i in range(0, n):
    line = input()
    if (not found) and 'p' in set(line):
        py = i
        found = True
    grid.append(line)

print(nextMove(n,r,c,grid, py))
