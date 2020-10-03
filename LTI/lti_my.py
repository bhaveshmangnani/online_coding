# keep alone letter and check if it appears again as it is shifted
def spcount(s,n):
    count=0
    ans=True

    alone=True
    sl=list(s)
    i=0
    char=None
    while i<n//2:
        cur=i
        curr=n-i-1
        if sl[cur]!=sl[curr]:
            pos=-1
            if curr-cur<=0:
                break
            for j in range(curr-1,cur,-1):
                if sl[j]==sl[cur]:
                    pos=j
                    break
            print(f"cur={cur} curr={curr} pos={pos}")
            print(sl)
            if pos<0:
                #print("in")
                if alone or sl[i]==char:
                    alone=False
                    char=sl[i]
                    t = sl[i]
                    sl[i]=sl[i+1]
                    sl[i+1] = t
                    count+=1
                    print(sl)
                    continue
                else:
                    ans=False
                    break
            #print(sl)
            for j in range(pos,curr):
                t = sl[j]
                sl[j] = sl[j+1]
                sl[j+1] = t
                count+=1
                print(sl,"for")
        i=i+1
    if ans:
        print(f"my={count}")
    else:
        print(-1)
            
def CountSwap(s, n): 
    s = list(s) 
  
    # Counter to count minimum swap 
    count = 0
    ans = True
  
    # A loop which run in half string 
    # from starting 
    for i in range(n): 
  
        # Left pointer 
        left = i 
  
        # Right pointer 
        right = n - left - 1
  
        # A loop which run from right pointer 
        # to left pointer 
        while left < right: 
  
            # if both char same then 
            # break the loop if not 
            # same then we have to move 
            # right pointer to one step left 
            if s[left] == s[right]: 
                break
            else: 
                right -= 1
  
        # it denotes both pointer at 
        # same position and we don't 
        # have sufficient char to make 
        # palindrome string 
        if left == right: 
            ans = False
            break
        else:
            #print("in")
            #print(s)
            #print(left,"lr",right)
            for j in range(right, n - left - 1):
                #print(s)
                (s[j], s[j + 1]) = (s[j + 1], s[j]) 
                count += 1
    print("GFG",count)

s="maamamma"
#s="niinininaa"
#
s="ntaiin"
#s="mama"
#s="mmaammaa"
s="mamad"
s= "nitn"
l=len(s)
print(s)
#CountSwap(s,l)
spcount(s,l)
  
