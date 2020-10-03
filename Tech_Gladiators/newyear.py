n=int(input())

for i in range(n):
    t=int(input())
    lst=[int(x) for x in input().split()]
    
    first=max(lst)

    firstindex=lst.index(first)

    lst.pop(firstindex)

    if firstindex < t-2:
        lst.pop(firstindex)
    if firstindex != 0:
        lst.pop(firstindex-1)
    

    second=max(lst)

    if first+second>first:
        print(second,first,sep='')
    else:
        print(first)
