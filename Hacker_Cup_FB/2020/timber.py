
def find_max(lst, n, left):
    if side:
        maxd = lst[0][1]
            start = 1
            while True:
                if start <n:
                    temp = lst[start-1][1]
                    for i in range(start,n):
                        if lst[i-1][0]+lst[i-1][1]==lst[i][0]:
                            temp = temp + last[i][1]
                        else:
                            temp = max(temp , lst[i][1])
                            start = i + 1
                            break
                    maxd = max(temp , maxd)
                else:
                    break



try :
    tc = input()
    for t in range(tc):
        n = input()
        lst=[]
        for i in range(n):
            p,h = input().split()
            lst.append([p,h])
        lst.sort(key = lambda ele : ele[0])
        
        
            
            
