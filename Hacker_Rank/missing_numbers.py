# URL: https://www.hackerrank.com/challenges/missing-numbers/problem

def missingNumbers(n, arr, m, brr):
    # Write your code here
    dct_original = {}
    dct_copy = {}
    keys = []
    min_n = min(m,n)
    for i in range(min_n):
        ele = arr[i]
        if ele in dct_copy:
            dct_copy[ele]+=1
        else:
            dct_copy[ele] = 1
        ele = brr[i]
        
        if ele in dct_original:
            dct_original[ele]+=1
        else:
            dct_original[ele] = 1
            keys.append(ele)
    
    for i in range(min_n, n):
        ele = arr[i]
        if ele in dct_copy:
            dct_copy[ele]+=1
        else:
            dct_copy[ele] = 1
        ele = brr[i]
    
    for i in range(min_n, m):
        ele = brr[i]
        
        if ele in dct_original:
            dct_original[ele]+=1
        else:
            dct_original[ele] = 1
            keys.append(ele)
    
    lst = []
    for key in keys:
        if dct_original[key] != dct_copy.get(key, 0):
            lst.append(key)
    return sorted(lst) 
  
