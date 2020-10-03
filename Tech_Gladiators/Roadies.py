t=int(input())

for _ in range(t):

    n=int(input())
    intboxes=[int(x) for x in input().split()]

    summax=0

    intboxes.sort(reverse=True)


    for k in range(n):
        tempsum=0
        tempanswer=[]
        count=0
        i=k
        while count<n:

            print("Box number =",intboxes[i])
            flag=1
            for j in tempanswer:
                if len( set(j).intersection(set(str(intboxes[i]))) ) !=0:
                    #print(f"set j={set(j)}\nsetstr={set(str(intboxes[i]))}")
                    flag=0
                    break

            if flag:
                tempsum+=intboxes[i]
                tempanswer.append(str(intboxes[i]))

            i=(i+1)%n
            count+=1

            #print(f"temp answer={tempanswer}")

        summax=max(tempsum,summax)



    print(summax)
