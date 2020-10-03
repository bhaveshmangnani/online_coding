class Node:
    def __init__(self,d):
        self.data=d
        self.next=None


for _ in range(int(input())):
    s=set()
    dct={}
    for _ in range(3):
        gt,ls=input().split()
        s.add(gt)
        s.add(ls)
        if gt not in dct:
            dct[gt]=Node(gt)
        if ls not in dct:
            dct[ls]=Node(ls)
        dct[gt].next = dct[ls]
    ls=list(s)
    #print(ls)
    og=ls[0]
    temp=og
    #print("og",temp)
    f=True
    for __ in range(3):
        if temp in dct:
            #print("in",temp)
            temp=dct[temp].next.data
        else:
            #print("b",temp)
            f=False
            break
    if f:
        f=temp==og
    if f:
        print("Valid")
    else:
        print("Invalid")
            
    
