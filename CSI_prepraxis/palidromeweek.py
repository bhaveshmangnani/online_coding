year=input()
iyear=year[2:]


month=int(year[-1:1:-1])



if month<13:
    date=[1,2,3,4,5,6,7,8,9,11,22]
    for i in date:
        print(f"{month}-{i}-{iyear}")
        
    
else:
    month=int(year[-1])
    start=int(year[2])*10
    date=[]
    for i in range(10):
        date.append(start+i)
    for i in date:
        print(f"{month}-{i}-{iyear}")
    
