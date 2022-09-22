#https://www.hackerrank.com/challenges/gem-stones
def gemstones(n, arr):
    
    resSet = set(arr[0])
    
    for i in range(1, n):
        resSet = resSet.intersection(set(arr[i]))
    
    return len(resSet)
