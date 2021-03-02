#URL: https://www.hackerrank.com/challenges/tree-top-view/problem?h_r=profile
def topView(root):
    #Write your code here
    
    def r_level(node, c_level):
        #print(node)
        if node:
            right = r_level(node.right,c_level+1)
            left = r_level(node.left,c_level-1)
            stack = [[node.info, c_level],]
            #print(stack)
            
            if right:
                stack = stack+right
            if left:
                stack=stack+left
            return stack
        else:
            return []
    def l_level(node, c_level):
        if node:
            right = l_level(node.right,c_level+1)
            left = l_level(node.left,c_level-1)
            stack = [[node.info, c_level],]
            
            if left:
                stack=stack+left
            if right:
                stack = stack+right
            return stack
        else:
            return []
        
        
    
    right = r_level(root.right,1)
    left = l_level(root.left,-1)
    maxr=maxl=0

    if right:
        maxr = max(right, key = lambda x : x[1])[-1]
    if left:
        maxl = min(left, key = lambda x : x[1])[-1]
    #print(right, maxr)
    #print(left,maxl)
    ll = []
    lr = {}
    cml = 0
    for data,level in left:
        if level<cml:
            ll.append(data)
            cml = level
        elif level>maxr:
            lr[level] = data
            #maxr = level
    
    rl = []
    rr = []
    cmr = 0
    for data,level in right:
        if level>cmr:
            rr.append(data)
            cmr = level
        elif level<maxl:
            rl.append(data)
            maxl = level
    
    ans = []
    #print("ll",ll)
    #print("lr",lr)
    #print("rl",rl)
    #print("rr",rr)
    if rl:
        ans+=rl[::-1]
    if ll:
        ans+=ll[::-1]
    ans+=[root.info,]
    if rr:
        ans+=rr
    if lr:
        #ans+=list(lr.values())
        temp = sorted(lr.items(), key = lambda x: x[0])
        temp2 = []
        for i in temp:
            temp2.append(i[1])
        ans+=temp2
    print(*ans)
