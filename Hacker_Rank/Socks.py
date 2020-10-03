n=int(input())

lst=[int(x) for x in input().split()]

count={}

for i in lst:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

sum1=0
for i in count.values():
    if i>1:
        sum1=sum1+i//2
print(sum1)
