import time


t=int(input())

for i in range(t):

    count=0
    nrows,ncolumns=[int(x) for x in input().split()]
    row=[int(x) for x in input().split()]
    column=[int(x) for x in input().split()]
    #print(f"row={row}\ncolumn={column}")
    start=time.time()
    if sum(row)!=sum(column):
        print("NO")
        continue

    flag=False
    rowindex=0
    columnindex=0
    for _ in range(nrows*ncolumns):

        rowindex=_%(nrows)
        columnindex=_%(ncolumns)
        for _1 in range(nrows*ncolumns):

            count+=1
            if columnindex==ncolumns-1:
                rowindex=(rowindex+1)%(nrows)

                
            #print(f"row index={rowindex}  columnindex={columnindex}")
            
            if row[rowindex]==0:
                rowindex=(rowindex+1)%(nrows)
                continue

            if column[columnindex]==0:
                columnindex=(columnindex+1)%(ncolumns)
                continue

            row[rowindex]-=1

            column[columnindex]-=1
            columnindex=(columnindex+1)

            #print(f"\n\nAfter increment\nrow index={rowindex}  columnindex={columnindex}")

            

            columnindex=columnindex%(ncolumns)


            if sum(row)==0 and sum(column)==0:
                flag=True
                break

    end=time.time()
    if flag:
        print(f"YES  {count} time={end-start}")
    else:
        print(f"NO  {count}  time={end-start}")
