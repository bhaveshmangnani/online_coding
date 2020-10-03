
fin = open("travel_restrictions_input.txt",'r')
testcases = int(fin.readline())
for t in range(testcases):
    n = int(fin.readline())
    incoming = [int( x=='Y') for x in fin.readline()[:n]]
    outgoing = [int( x=='Y') for x in fin.readline()[:n]]

    outmat = []

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append('Y')
        outmat.append(temp)

    for i in range(n):

        f = outgoing[i]
        if f:
            left = None
            for j in range(i-1,-1,-1):
                if not incoming[j]:
                    left = j
                    break
                if not outgoing[j]:
                    left = j-1
                    break
            if left != None:
                for j in range(left,-1,-1):
                    outmat[i][j]='N'
                left = None
                
            for j in range(i+1,n):
                if not incoming[j]:
                    left = j
                    break
                if not outgoing[j]:
                    left = j+1
                    break
            if left!=None:
                for j in range(left,n):
                    outmat[i][j]='N'
        else:
            for j in range(i-1,-1,-1):
                outmat[i][j]='N'
            for j in range(i+1,n):
                outmat[i][j]='N'
    foutput = open('travel_restriction_final.txt','a')
    foutput.write('Case #'+str(t+1)+":\n")
    
    for i in range(n):
        for j in range(n):
            foutput.write(outmat[i][j])
        foutput.write("\n")
    foutput.close()   
fin.close()

