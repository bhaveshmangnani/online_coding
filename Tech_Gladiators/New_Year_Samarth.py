class House:
    def __init__(self,value,index):
        self.value=value
        self.index=index


def custom(ele):
    return ele.value

def customsort2(ele):
    return ele.index

t=int(input())
for k in range(t):
    objectlist=[]
    n=int(input())
    lst=[int(x) for x in input().split()]
    for i in range(n):
        obj=House(lst[i],i)
        objectlist.append(obj)
    
    
    sortedobjectlist=sorted(objectlist,key=custom,reverse=True)
    

    finalsum=0
    finalqueue=[]

    i=0
    for j in range(n):
        i=j
        tempsum=0
        tempcovered=set()
        tempqueue=[]
        while i<n:
            if sortedobjectlist[i].value<=0:
                break
            ti=sortedobjectlist[i].index
            a,b=ti-1,ti+1
            if a in tempcovered or b in tempcovered:
                pass
            else:
                tempsum+=sortedobjectlist[i].value
                tempcovered.add(ti)
                tempqueue.insert(0,sortedobjectlist[i])
            i+=1
        if tempsum>finalsum:
            finalsum=tempsum
            finalcovered=tempcovered.copy()
            finalqueue=[tempqueue.copy()]
        elif tempsum==finalsum:
            finalqueue.append(tempqueue)
        else:
            break

    for house in finalqueue:
        house.sort(key=customsort2,reverse=True)

    finalanswer=[]
    for j in finalqueue:
        answer=""
        for k in j:
            temp=str(k.value)
            answer+=temp
        finalanswer.append(answer)
    
    finalanswer.sort(reverse=True)
    print(finalanswer[0])
