h,w=[int(x) for x in input().split()]
mat=[]
for i in range(h):
    row=[int(x) for x in input().split()]
    mat.append(row)


sa=h*w+mat[0][0]*2+1

    

if h>1:
    for i in range(1,w):
        ans=mat[0][i]+abs(mat[0][i]-mat[0][i-1])+1
        if mat[0][i]>mat[1][i]:
            ans+=mat[0][i]-mat[1][i]
        sa+=ans
    sa+=mat[0][-1]
    for i in range(1,h-1):
        ans=mat[i][0]+1
        
        if mat[i][0]>mat[i-1][0]:
            ans+=mat[i][0]-mat[i-1][0]

        if mat[i][0]>mat[i+1][0]:
            ans+=mat[i][0]-mat[i+1][0]
        
        
        for j in range(1,w):
            ans+=abs(mat[i][j]-mat[i][j-1])+1
            if mat[i][j]>mat[i-1][j]:
                ans+=mat[i][j]-mat[i-1][j]

            if mat[i][j]>mat[i+1][j]:
                ans+=mat[i][j]-mat[i+1][j]

            
        ans+=mat[i][-1]
        sa+=ans
    sa+=mat[-1][0]*2+1# for 1,1 /n 1 mistake
    for i in range(1,w):
        ans=mat[-1][i]+abs(mat[-1][i]-mat[-1][i-1])+1
        if mat[-1][i]>mat[-2][i]:
            ans+=mat[-1][i]-mat[-2][i]
        
        
        sa+=ans
    sa+=mat[-1][-1]
else:
    for i in range(1,w):
        ans=mat[0][i]+abs(mat[0][i]-mat[0][i-1])+1
        sa+=ans
    for i in range(w):
        sa+=mat[0][i]
    sa+=mat[0][-1]
    
print(sa)






