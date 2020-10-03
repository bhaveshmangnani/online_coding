import time as D
n,k=[int(x) for x in input().split()]
qy,qx=[int(x) for x in input().split()]
obs=[]
moves=2*(n-1) + min(qx-1,qy-1) + min(qx-1, n-qy) + min(n-qx, n-qy) + min(n-qx, qy-1)
r=set()
c=set()
D1=set()
D2=set()
s=D.time()
for i in range(k):
    oy,ox=[int(x) for x in input().split()]
    if ox==qx:
        c.add((oy,ox))
    elif oy==qy:
        r.add((oy,ox))
    else:
        d1 = ox-oy-qx+qy
        if d1:
            d2=ox+oy-qx-qy
            if not d2:
                D2.add((oy,ox))
        else:
            D1.add((oy,ox))

if r:
    rx1,rx2,=n+1,0
    temp=list(r)
    ry=temp[0][0]
    for i in temp:
        tx=i[1]
        d=qx-tx
        if tx>qx and tx<rx1:
            rx1=tx
        elif tx<qx and tx>rx2:
            rx2=tx
    if rx1!=(n+1):
        obs.append((ry,rx1))
    if rx2:
        obs.append((ry,rx2))
    r=None

if c:
    cy1,cy2=n+1,0
    temp=list(c)
    cx=temp[0][1]
    for i in temp:
        ty=i[0]
        if ty>qy and ty<cy1:
            cy1=ty
        elif ty<qy and ty>cy2:
            cy2=ty
    if cy1!=(n+1):
        obs.append((cy1,cx))
    if cy2:
        obs.append((cy2,cx))
    
if D1:
    dy1,dy2=(n+1),0
    temp=list(D1)
    dx1=dx2=temp[0][1]
    for i in temp:
        ty = i[0]
        if ty>qy and ty<dy1:
            dy1=ty
            dx1=i[1]
        elif ty<qy and ty>dy2:
            dy2=ty
            dx2=i[1]
    if dy1!=(n+1):
        obs.append((dy1,dx1))
    if dy2:
        obs.append((dy2,dx2))
    
if D2:
    dy1,dy2=(n+1),0
    temp=list(D2)
    dx1=dx2=temp[0][1]
    for i in temp:
        ty = i[0]
        if ty>qy and ty<dy1:
            dy1=ty
            dx1=i[1]
        elif ty<qy and ty>dy2:
            dy2=ty
            dx2=i[1]
    if dy1!=(n+1):
        obs.append((dy1,dx1))
    if dy2:
        obs.append((dy2,dx2))

#print(obs)
for i in obs:
    oy,ox=i
    if ox==qx:
        if oy>qy:
            moves = moves-(n-oy+1)
        else:
            moves-=oy
    if oy==qy:
        if ox>qx:
            moves-=(n-ox+1)
        else:
            moves-=ox
    d1 = ox+oy-qx-qy
    if not d1:
        if oy>qy:
            moves-=(min(ox-1,n-oy)+1)
        else:
            moves-=(min(n-ox,oy-1)+1)

    else:
        d2=ox-oy-qx+qy
        if not d2:
            if ox>qx:
                moves-=(min(n-ox, n-oy)+1)
            else:
                moves-=(min(ox-1, oy-1)+1)
    #print("obs=",i,"\nm=",moves)
e=D.time()
f=e-s
print(moves,"t=",f)
