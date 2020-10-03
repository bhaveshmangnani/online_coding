


t=int(input())




def checkValid(current,tempans):

    for i in current:
        if i in tempans:
            return False
    return True





for i in range(t):

    n=int(input())

    boxes=[int(x) for x in input().split()]
    boxes.sort(reverse=True)
    summax=0

    for j in range(n):

        tempsum=boxes[j]
        tempans=[ int(x) for x in str(boxes[j])]
        count=0
        k=(j+1)%n
        while count<n:

            currentlist=[int(x) for x in str(boxes[k])]

            if checkValid(currentlist,tempans):

                tempsum+=boxes[k]
                tempans.extend(currentlist)

            k=(k+1)%n
            count+=1

            print(f"tempsum={tempsum}\ntempans={tempans}\n\n")






        summax=max(summax,tempsum)

    
    print(summax)
