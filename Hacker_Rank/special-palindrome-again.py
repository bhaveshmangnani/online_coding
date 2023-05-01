#https://www.hackerrank.com/challenges/special-palindrome-again

def substrCount(n, s):
    
    ans = n
    i=1
    current = s[0]
    other = None
    otherIndex = None
    left = 1
    right = 0
    while i<n:
        if(s[i] != current):
            if(other == None):
                other = s[i]
                otherIndex = i
            else :
                
                minLR = min(left, right)
                ans += ( minLR + (left*(left+1)/2) -left)
                current = s[otherIndex]
                i = otherIndex
                other = None
                otherIndex = None
                left = 1
                right = 0
        else:
            if(other == None):
                left +=1
            else:
                right += 1
                    
        #print(f"curr {current} si = {s[i]} left= {left} r= {right} ans = {ans} oi= {otherIndex}")
        i+=1
    minLR = min(left, right)
    left_add = ((left*(left+1)/2) -left )
    ans += (minLR + left_add + right*(right + 1)/2 - right)
    # if(otherIndex != None):
    #     ans += (n - otherIndex)
    return int(ans)
