#URL : https://www.hackerrank.com/challenges/count-triplets-1
def countTriplets(n, arr, r):
    
    res = 0
    
    left = {}
    right = {}
    
    for i in arr:
        
        right[i] = right.get(i, 0) + 1
        left[i] = 0
    
    for index in range(n):
        
        i = arr[index]
        
        right[i] -= 1
        prev, nxt = i/r, i*r
        
        if prev in left and nxt in right:
            res += (left[prev] * right[nxt])
        
        left[i] += 1
    return res
