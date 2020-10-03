
fh = open("travel_restrictions_input.txt",'r')
try:
    tc = int(fh.readline())
    for t in range(tc):
        n = int(fh.readline())
        inc = [int( x=='Y') for x in fh.readline()[:n]]
        out = [int( x=='Y') for x in fh.readline()[:n]]

        op = []

        for i in range(n):
            temp = []
            for j in range(n):
                temp.append('Y')
            op.append(temp)

        for i in range(n):

            f = out[i]
            if f:
                more = None
                for j in range(i-1,-1,-1):
                    if not inc[j]:
                        more = j
                        break
                    if not out[j]:
                        more = j-1
                        break
                if more != None:
                    for j in range(more,-1,-1):
                        op[i][j]='N'
                    more = None
                    
                for j in range(i+1,n):
                    if not inc[j]:
                        more = j
                        break
                    if not out[j]:
                        more = j+1
                        break
                if more!=None:
                    for j in range(more,n):
                        op[i][j]='N'
            else:
                for j in range(i-1,-1,-1):
                    op[i][j]='N'
                for j in range(i+1,n):
                    op[i][j]='N'
        fop = open('travel_restriction_final.txt','a')
        fop.write('Case #'+str(t+1)+":\n")
        
        for i in range(n):
            for j in range(n):
                fop.write(op[i][j])
            fop.write("\n")
        fop.close()
        
finally:
    fh.close()

