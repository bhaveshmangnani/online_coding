



t=int(input())

for i in range(t):
    n=int(input())

    lst=[int(x) for x in input().split()]
    visited=[]
    answer=[]
    summax=max(lst)
    visited.append(lst.index(summax))
    answer.append(summax)

    for j in range(n):
        
        tempsum=lst[j]
        tempanswer=[lst[j]]
        tempvisited=[j]

        print("J loop")
        print(f"temp sum={tempsum} tempans={tempanswer} tempvisited={tempvisited}\n\n")
        for k in range(n):
            

            if int(k+1) in tempvisited or int(k-1) in tempvisited or k in tempvisited:
                continue

            else:
                if tempsum +lst[k]>tempsum:
                    tempanswer.append(lst[k])
                    tempsum+=lst[k]
                    tempvisited.append(k)

            print("K loop")
            print(f"temp sum={tempsum} tempans={tempanswer} tempvisited={tempvisited}\n\n")


        if tempsum>summax:
            answer=tempanswer.copy()
            summax=tempsum
            visited=tempvisited.copy()
            continue

        if tempsum==summax:
            if set(visited)==set(tempvisited):
                continue
            print("IN EQUAL")
            if answer[-1]<tempanswer[-1]:
                answer=tempanswer.copy()
                summax=tempsum
                visited=tempvisited.copy()

                
            else:

                print("in equal")
                continue

    answer=answer[::-1]
    for k in answer:
        print(k,end='')
    
    print()

        








