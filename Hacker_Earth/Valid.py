a=("A","E","I","O","U")
st=input()
flag =1
num=[]
for x in st:
    if x.isdigit():
        num.append(int(x))
        
print(num)        
for i in range(len(num)-1):
    print(num[i]+num[i+1])
    if (num[i]+num[i+1])%2 != 0:
        flag =0
        print("Break")
        break
    
    
if st[2] in a:
    flag =0
if flag :
    print("valid")
else:
    print("invalid")