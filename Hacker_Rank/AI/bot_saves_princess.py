#URL: https://www.hackerrank.com/challenges/saveprincess/problem

def displayPathtoPrincess(n,grid):
    P=[]
    M=[]
    i=0
    for string in grid:
        #string = input().strip()
    
        if not P:
            for j in range(m):
                if string[j]=='p':
                    P = [i,j]

        if not M:
            for j in range(m):
                if string[j]=='m':
                    M = [i,j]
        i+=1
    X = -P[0]+M[0]
    op = "UP"
    if X<0:
        op = "DOWN"
        X=X*(-1)
    for i in range(X):
        print(op)
    op = "RIGHT"

    Y=P[1]-M[1]
    if Y<0:
        op = "LEFT"
        Y=(-1)*Y
    for i in range(Y):
        print(op)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
