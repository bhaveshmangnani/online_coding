#https://www.hackerrank.com/challenges/closest-numbers
def closestNumbers(n, arr):
    
    arr.sort()
    minDiff = abs(arr[0] - arr[1])
    res = [arr[0], arr[1]]
    
    for i in range(2, n):
        diff = abs(arr[i] - arr[i-1])
        curRes = [arr[i-1], arr[i]]
        
        if diff < minDiff :
            minDiff = diff
            res = curRes
        elif diff == minDiff:
            res.extend( curRes )
    
    return res
