t=int(input())

for i in range(t):

    rows,columns=[int(x) for x in input().split()]
    rowlist=[int(x) for x in input().split()]
    columnlist=[int(x) for x in input().split()]
    flag=1

    if sum(rowlist)!=sum(columnlist):
        print("NO")
        continue

    for j in columnlist:
        if j>rows:
            flag=0
            break
    if flag:
        for j in rowlist:
            if j>columns:
                flag=0
                break

    if flag:
        print("YES")
    else:
        print("NO")
