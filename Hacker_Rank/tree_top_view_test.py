class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
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
    print(right, maxr)
    print(left,maxl)
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
    a2 = topView1(root)
    if ans !=a2:
        print("THIS ONE")
    

def topView1(root):
    from queue import Queue
    uniq_lvls = []
    level_set = set()
    q = Queue()
    q.put((root, 0))
    
    while not q.empty():
        
        temp = q.get()
        if temp[1] not in level_set:
            uniq_lvls.append(temp)
            level_set.add(temp[1])
        if temp[0].left:
            q.put((temp[0].left, temp[1]-1))
        if temp[0].right:
            q.put((temp[0].right, temp[1]+1))
    ans = []
    for x in sorted(uniq_lvls, key=lambda e: e[1]):
        print(x[0].info, end=' ')
        ans.append(x[0].info)
    return ans
    

def start():
    
    import random
    tree = BinarySearchTree()
    t = random.randint(5,20)

    #arr = list(map(int, input().split()))
    arr = []
    print("------------"*3)
    
    print(t)
    for i in range(t):
        arr.append(random.randint(1,100))
    print(*arr)
    

    for i in range(t):
        tree.create(arr[i])
    print("============"*3)

    topView(tree.root)
    print()
    print("============"*3)
def tc1():
    arr = [99, 9, 47, 38, 94, 8, 99, 1, 57, 13, 20, 29, 34, 72, 21, 8, 98, 35, 29, 51]
    tree = BinarySearchTree()
    for i in arr:
        tree.create(i)
    r = tree.root
    topView(r)
