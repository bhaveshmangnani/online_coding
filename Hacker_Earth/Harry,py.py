st=[int(x) for x in input()]
if len(st) != 10:
    print("Illegal ISBN")
else:
    sum1=0
    for x in range(1,11):
        sum1+=x*st[x-1]
        print(sum1)
    if sum1%11==0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")