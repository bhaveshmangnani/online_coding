#URL:https://www.hackerrank.com/challenges/no-idea/problem


n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
A = set(int(x) for x in input().split())
B = set(int(x) for x in input().split())

score = 0

for i in arr:
    if i in A:
        score+=1
    elif i in B:
        score-=1
print(score)
