#URL: https://www.hackerrank.com/challenges/s10-quartiles/problem

def quartiles(n, arr):
    # Write your code here
    arr.sort()
    q1=q2=q3=0
    
    q_dct={}
    
    if n%4==0:
        mid = n//2
        q1 = n//4
        
        q_dct[2] = [arr[mid-1], arr[mid]]
        q_dct[1] = [arr[q1-1],arr[q1]]
        q_dct[3] = [arr[q1+mid-1], arr[q1+mid]]
        
    elif n%4==1:
        mid = n//2
        q1 = n//4
        
        q_dct[2] = [arr[mid]]
        q_dct[1] = [arr[q1-1], arr[q1]]
        q_dct[3] = [arr[q1+mid], arr[q1+mid+1]]
        
    elif n%4==2:
        mid = n//2
        q1 = n//4
        
        q_dct[2] = [arr[mid-1], arr[mid]]
        q_dct[1] = [arr[q1]]
        q_dct[3] = [arr[q1+mid]]
    else:
        mid = n//2
        q1 = n//4
        
        q_dct[2] = [arr[mid]]
        q_dct[1] = [arr[q1]]
        q_dct[3] = [arr[q1+mid+1]]
    q1 = sum(q_dct[1])//len(q_dct[1])
    q2 = sum(q_dct[2])//len(q_dct[2])
    q3 = sum(q_dct[3])//len(q_dct[3])
    
    return q1,q2,q3
