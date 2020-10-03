n,k,q=[int(x) for x in input().split()]
ar=[int(x) for x in input().split()]
for i in range(q):
    ele=int(input())
    print(ar[(k%n+ele-1)%n])
