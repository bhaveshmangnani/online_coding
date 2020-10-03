n,m=[int(x) for x in input().split()]

operations=[]

for i in range(m):
    operations.append([int(x) for x in input().split()])
    

s1=set(range(operations[0][0],operations[0][1]))
s2=set(range(operations[1][0],operations[1][1]))
iop=s1.intersection(s2)
for i in range(2,m):
    s3=set(range(operations[i][0],operations[i][1]))
    iop=iop.intersection(s3)
           
print(num)
num=list(iop)[0]
print(num)
           
           
ans=0 
for i in range(m):
           if num>=operations[i][0] and num<=operations[i][1]:
            ans=ans+operations[i][k]

print(ans)
