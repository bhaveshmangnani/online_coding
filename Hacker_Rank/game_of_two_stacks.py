#URL: https://www.hackerrank.com/challenges/game-of-two-stacks/problem
def solve(n, m, a, b, summax):
    tot = 0
    score = 0
    for i in range(n):
        if tot+a[i]>summax:
            break
        tot+=a[i]
        score+=1
    
    top1 = score-1
    maxscore = score
    for j in range(m):
        if tot+b[j]>summax:
            if top1==-1:
                break
            else:
                while top1>-1:
                    if tot+b[j]>summax:
                        tot-=a[top1]
                        top1-=1
                        score-=1
                    else:
                        break
        
        tot+=b[j]
        score+=1
        maxscore = max(score,maxscore)
    return maxscore

for _ in range(int(input())):
    n,m,summax = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    score1 = solve(n, m, a, b, summax)
    score2 = solve(m, n, b, a, summax)
    score = max( score1 , score2 )        
    print(score)
