#URL: https://www.hackerrank.com/challenges/sherlock-and-array/problem

def balancedSums(n, arr):
    # Write your code here
    if n==1:
        return "YES"
    right_sum = sum(arr[1:])
    left_sum = 0
    for i in range(1,n):
        #print(f"l={left_sum} r={right_sum} ar={arr[i]}")
        if left_sum == right_sum :
            return "YES"
        else:
            left_sum+=arr[i-1]
            right_sum-=arr[i]
    return "NO"
