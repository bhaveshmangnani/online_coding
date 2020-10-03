import random


def calculate(n,x):
    leftodd1 = [0]*n
    rightodd1 = [0]*n
    cleft1 = 0
    cright1 = 0
    for i in range(n):
        if x[i]%2 == 1:
            cleft1 +=1
        else:
            if x[i]%4 == 0:
                cleft1 = 0
            else:
                leftodd1[i] = cleft1
                cleft1 = 0

    for i in range(n):
        if x[n-i-1]%2 == 1:
            cright1 +=1
        else:
            if x[n-i-1]%4==0:
                cright1 = 0
            else:
                rightodd1[n-i-1] = cright1
                cright1 = 0
    total = 0
    for i in range(n):
        if x[i]%4 == 2:
            total+= (leftodd1[i] * rightodd1[i]) + leftodd1[i] + rightodd1[i] + 1

    totsum = int((n*(n+1))/2) - total
    return totsum

def bruteforce(lst,n):
	cont=0
	for i in range(n):
		prod=1
		for j in range(i,n):
			prod*=lst[j]
			if prod%4==2:
				cont+=1
	total=(n*(n+1))//2
	#print(total-cont)
	return total-cont

def effecient(lst,n):
    count,i,pointer,prev=0,0,0,-2
    while i<n:
        if lst[i]%4==2:
            #print("YES")
            if prev<0:
                prev=pointer+0
                pointer=0
                i+=1
                continue
            if prev>=0:
                count+=pointer+prev+1+prev*pointer
            prev=pointer+0
            pointer=0
        elif lst[i]%2==0:
            print("in")
            if prev>=0:
                count+=pointer+prev+1+prev*pointer
            pointer,prev=0,-1
        else:
            pointer+=1
        i+=1
    if prev>=0:
        #print("Incrementing after loop")
        count+=pointer+prev+1+pointer*prev
    total=(n*(n+1))//2
    #print("Count:",count)
    #print(total-count)
    return total-count

t=100
for _ in range(t):
    n=random.randint(1,15)
    lst=[0,-1,1,2]
    for i in range(n):
        lst.append(random.randint(1,50))
    #print(lst) 
    if calculate(len(lst),lst)!=effecient(lst,len(lst)):
        print(lst,len(lst))
        print("Gadbad hai")
    else:
        pass
        #print("Fine")
print("Done")
        
