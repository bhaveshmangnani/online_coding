
def custom(ele):
    return ele[0]




t=int(input())

for i in range(t):
    n=int(input())

    lst=[int(x) for x in input().split()]

    mainlist=[]
    answer=[]
    visited=[]

    for temp in range(n):
        templst=[]
        templst.append(lst[temp])
        templst.append(temp)
        mainlist.append(templst)

    mainlist.sort(key=custom,reverse=True)

    summax=0

    for j in range(n):
        
        if j==0:
            summax+=mainlist[j][0]
            answer.append(mainlist[j])
            visited.append(mainlist[j][1])
        
        else:
            if (int(mainlist[j][1]+1) in visited) or (int(mainlist[j][1]-1) in visited):
                continue
            
            if summax + mainlist[j][0] > summax:
                summax+=mainlist[j][0]
                answer.append(mainlist[j])
                visited.append(mainlist[j][1])


        print(visited)


    for ans in answer:
        print(ans[0],end='')
    
    print()
