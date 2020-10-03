
for case in range(int(input())):

    n = int(input())
    lst=[]
    r = 0
    c = 0
    trace = 0
    for i in range(n):
        rl = [int(x) for x in input().split()]
        if len(set(rl))!=n:
            r = r+1
        lst.append(rl)
        
    for i in range(n):
        trace = trace + lst[i][i]
        temp = set()
        for j in range(n):
            temp.add(lst[j][i])
        if len(temp)!=n:
            c = c+1
    print(f"Case#{case}: {trace} {r} {c}")
