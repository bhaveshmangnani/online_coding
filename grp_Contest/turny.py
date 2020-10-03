class Node:
    def __init__(self,d):
        self.data=d
        self.pos=None
        self.lpos=None

def search_tree(root,ele):
    if root.left.data==ele:
        return 0
    elif root.right.data==ele:
        return 1
    else:
        c=0
        c+=search_tree(root.left,ele)
        c=c+search_tree(root.right,ele)


for _ in range(int(input())):
    tree=[Node(x) for x in input().split()]
    n=len(tree)
    f,s=[int(x) for x in input().split()]
    root=tree[0]
    root.pos=""
    root.lpos=0
    i=0
    j=1
    while j<n:
        tree[i].left=tree[j]
        tree[j].pos=tree[i].pos+"L"
        tree[j].lpos=tree[i].lpos+1
        
        tree[i].right=tree[j+1]
        tree[j+1].pos=tree[i].pos+"R"
        tree[j+1].lpos=tree[i].lpos+1
        i+=1
        j+=2
    
    for i in range(n):
        #print(tree[i].data,f)
        if tree[i].data==str(f):
            f=i
            break
    for i in range(n):
        if tree[i].data==str(s):
            s=i
            break
    finalstr=tree[f].pos[::-1]+tree[s].pos
    ans=0
    #print(finalstr)
    for i in range(1,tree[f].lpos+tree[s].lpos):
        if finalstr[i]!=finalstr[i-1]:
            ans+=1
    if ans:
        print(ans)
    else:
        print(-1)
    
