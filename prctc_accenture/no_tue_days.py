
ed = 6

def check_leap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year % 4==0:
        return True
    return False

prev = None

check_day = 2
cnt = 0

for year in range(2000,3001):
    if check_day == ed:
        #print("in")
        cnt+=1
    if check_leap(year):
        #print("in1")
        if check_day ==ed+1:
            cnt +=1
        ed+=1
    
        
    cnt+=52
    
    ed = (ed+1)%7
print(cnt)
    
    
