#URL: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

n = int(input())

arr = list(map(int,input().split()))
arr.sort()

mean = 0
meadian = 0
mode = 0

if n%2:
    meadian = arr[n//2]
else:
    i = n//2
    meadian = (arr[i-1] + arr[i])/2

mean = max_ele = arr[0]
max_cnt = 1
te = arr[0]
temp_cnt = 1

for i in range(1,n):
    mean+=arr[i]
    if arr[i]==arr[i-1]:
        temp_cnt+=1
    else:
        if temp_cnt > max_cnt:
            max_ele = te
            max_cnt = temp_cnt
        else:
            temp_cnt=1
            te=arr[i]
print(round(mean/n,1), round(meadian,1), round(max_ele,1), sep = "\n")
