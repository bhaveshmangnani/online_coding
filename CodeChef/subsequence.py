t=int(input())

for _ in range(t):
    n,k=[int(x) for x in input().split()]
    lst=[int(x) for x in input().split()]
    lst.sort()
    print(sum(lst[:k]))
