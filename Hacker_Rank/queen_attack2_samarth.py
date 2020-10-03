import time
def in_range(i,j):
    if (i>n) or (i<1):
        return False
    if j>n or j<1:
        return False
    return True

def go_up(i,j):
    while True:
        #print(i)
        i+=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_down(i,j):
    while True:
        i-=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_right(i,j):
    while True:
        j+=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_left(i,j):
    while True:
        j-=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_upleft(i,j):
    while True:
        i+=1
        j-=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_downright(i,j):
    while True:
        i-=1
        j+=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break

def go_upright(i,j):
    while True:
        i+=1
        j+=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break
def go_downleft(i,j):
    while True:
        i-=1
        j-=1
        if in_range(i,j):
            if (i,j) in obstacles:
                break
            else:
                C.count+=1
        else:
            break

obstacles=set()
class C:
    count=0
n,k=[int(x) for x in input().split()]
qi,qj=[int(x) for x in input().split()]
for m in range(k):
    ti,tj=[int(x) for x in input().split()]
    obstacles.add((ti,tj))
#print(obstacles)
s=time.time()
go_up(qi,qj)
go_down(qi,qj)
go_upleft(qi,qj)
go_upright(qi,qj)
go_right(qi,qj)
go_left(qi,qj)
go_downleft(qi,qj)
go_downright(qi,qj)
e = time.time()
f=e-s
print(C.count,"t=",f)
