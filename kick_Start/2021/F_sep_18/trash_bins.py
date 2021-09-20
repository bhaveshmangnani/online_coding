
for case in range(int(input())):
    
    n = int(input())
    arr = list(map(int,input()))
    
    prev_next =[]
    prev = None
    t_next = None

    pn_n = 0

    for i in range(n):
        if arr[i] == 1:
            
            prev = t_next
            t_next = i
        
            prev_next.append([prev, t_next])
            pn_n+=1
    prev_next.append([prev_next[-1][1], None])
    #print(*prev_next)
    
    current = 0
    ans = 0
    for i in range(n):
        p,N = prev_next[current]
        if N!=None and i > N:
            current +=1
            p,N = prev_next[current]
        left = right = None

        t_ans = n
        if p!=None:
            left = i-p
            t_ans = left
        if N!=None:
            right = N-i
            t_ans = min(t_ans,right)
        ans+=t_ans
        #print(f"{i} -> {t_ans}")
    print(f"Case #{case+1}: {ans}")
        
