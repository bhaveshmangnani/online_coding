
for case in range(int(input())):
    
    n= int(input())
    rlst=[]
    clst=[]
    for i in range(n):
        td={}
        for i in range(1,n+1):
            td[i]=0
        rlst.append(td)
        clst.append(td.copy())

    row=0
    column=0
    for i in range(n):
        tl=[int(x) for x in input().split()]
        for i in range(n):
            rlst[row][tl[i]]+=1
            clst[i][tl[i]]+=1
        row+=1
        

    
        
    #print("Case#%d: %d %d %d"%(case,t,r,cd))        
                
