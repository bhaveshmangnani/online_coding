r1=6
c1=7
s1=[".......","...O...","....O..",".......","OO.....","OO....."]
s2=[".......","...O.O.","....O..","..O....","OO...OO","OO.O..."]
t1=3
rs1=["OOO.OOO","OO...OO","OOO...O","..OO.OO","...OOOO","...OOOO"]
t2=5
rs2=[".......","...O.O.","...OO..","..OOOO.","OOOOOOO","OOOOOOO"]
temp=[]
s1=s2

for sec in range(1,10):
    print("-"*10,f"after{sec}secs","-"*10)
    for i in s1:
        print(i)
    if sec%2:
        temp=s1
        s1=[]
        for _ in range(r1):
            s1.append("O"*c1)
    else:
        temp1=s1
        s1=[]
        for i in temp1:
            s1.append(list(i))
        for row in range(r1):

            for column in range(c1):

                if temp[row][column] == "O":
                    if row>-1:
                        s1[row][column]="."
                        if column-1>-1:
                            s1[row][column-1]="."
                        if column+1<c1:
                            s1[row][column+1]="."
                                   
                    if column>-1:
                        s1[row][column]="."
                        if row-1>-1:
                            s1[row-1][column]="."
                        if row+1<r1:
                            s1[row+1][column]="."
        temp1=s1
        s1=[]
        for i in temp1:
            s1.append("".join(i))
        
                        
        
        
