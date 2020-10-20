
def check_word(main, copy):
    #print(main, "<m c>",copy)
    n = len(main)
    m = len(copy)
    tm = min(m,n)
    for i in range(tm):
        if main[i]!=copy[i]:
            return i,False
    if m==n:
        return tm-1,True
    return tm-1,False


for case in range(int(input())):
    
    string = input()
    n = len(string)
    i = n-1
    scnt = 0
    cnt = 0
    while i>=0:
        _,valid = check_word("START", string[i:min(i+5,n)])
        if valid:
            scnt = scnt + 1
        _, valid = check_word("KICK", string[i:min(i+4,n)])
        
        if valid:
            cnt = cnt + scnt
        
        i = i-1
    print("Case #{}: {}".format(case+1,cnt))
        
        
        
    
    
