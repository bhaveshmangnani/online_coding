
def ac(a,b,x):
    a.reverse()
    b.reverse()
    stack = []
    total, score = 0, 0

    while a:
        item = a.pop()
        if (total + item) <= x:
            total += item
            score += 1
            stack.append(item)
        else: break
    
    maxScore = score

    while b:
        item = b.pop()
        total += item
        score += 1
        while total > x and stack:
            total -= stack.pop()
            score -= 1
        if total <= x and score > maxScore: maxScore = score
    
    return maxScore



def correct(n,m,a,b,x):
    total = 0
    atmp = []
    for i in range(n):
        val = a.pop()
        if total + val > x:
            break
        total += val 
        atmp.append(val)

    max_count = len(atmp)
    cur_count = max_count
    while m:
        if total + b[-1] <= x:
            total += b.pop() 
            m -= 1
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        total -= aval
        cur_count -= 1
    return max_count



def n_m(n, m, a, b, summax):
    maxscore = 0 
    tot = 0
    for i in range(n):
        tot +=a[i]
        if tot>summax:
            break
        ts = tot
        score = i+1
        for j in range(m):
            if ts+b[j]>summax:
                break
            score+=1
            ts+=b[j]
        maxscore = max(score, maxscore)
    tot=0
    for i in range(m):
        tot +=b[i]
        if tot>summax:
            break
        ts = tot
        score = i+1
        for j in range(n):
            if ts+a[j]>summax:
                break
            score+=1
            ts+=a[j]
        maxscore = max(score, maxscore)
            
    return maxscore




def solve(n, m, a, b, summax):
    
    tot = 0
    score = 0
    
    for i in range(n):
        if tot+a[i]>summax:
            break
        tot+=a[i]
        score+=1
    #print("in func",score, tot)
    top1 = score-1
    maxscore = score
    for j in range(m):
        if tot+b[j]>summax:
            if top1==-1:
                break
            else:
                while top1>-1:
                    if tot+b[j]>summax:
                        tot-=a[top1]
                        top1-=1
                        score-=1
                    else:
                        break                    
                
                #print("in",j)
                #if tot+
                #tot+=(b[j])
                #score+=1
                #top1-=1
        
        tot+=b[j]
        score+=1
        #print("in func2",score, tot)
        maxscore = max(score,maxscore)
    return maxscore



def start(g):

    for _ in range(g):
        #n,m,summax = map(int,input().split())
        #a = list(map(int,input().split()))
        #b = list(map(int,input().split()))
        import random
        n = random.randint(1,15)
        m = random.randint(1,15)
        summax = random.randint(1,10000)
        a =[]
        b = []
        for _ in range(n):
            t = random.randint(0,1000)
            a.append(t)
        for _ in range(m):
            t = random.randint(0,1000)
            b.append(t)
        a_copy = a.copy()
        b_copy = b.copy()
            
        score2 = solve(m, n, b, a, summax)
        
        score1 = solve(n, m, a, b, summax)
        #print(score1, score2)
        score = max( score1 , score2  )
        nms = n_m(n, m, a, b, summax)
        final =ac(a,b,summax)
        print(f"----------score={score} nm = {nms}  correct ={final}----------")
        if score-nms or nms-final:
            print("==============="*3)
            print(n, m, summax)
            print(a_copy)
            print(b_copy)
            print("==============="*3)
