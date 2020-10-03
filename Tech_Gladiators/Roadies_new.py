t=int(input())

for j in range(t):

    n=int(input())

    intboxes=[int(x) for x in input().split()]
    

    
    summax=0
    
    for i in range(n):
        tempsum=0
        tempvisited=[]
        while len(tempvisited)<10 and len(intboxes)>0:
            print("**********************************")
            flag=1
            current=intboxes[i]
            print(f"current={current}")
            cset=list(str(current))
            print(f"cset={cset}")
            for k in cset:
                print(f"k={k}\nvisited={tempvisited}")
                #print(k in visited)

                if k in tempvisited:
                    print("in unvisited")
                    flag=0
                    break
                    
                    
            print(f"flag = {flag}")
            if flag:
                for k in cset:
                    tempvisited.append(k)
                tempsum+=current
                
            
            i=(i)%(len(intboxes))
            intboxes.remove(current)
            print(f"temsum={tempsum}")

        summax=max(summax,tempsum)
        

    print(summax)
