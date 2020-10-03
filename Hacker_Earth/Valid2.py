a=("A","E","I","O","U","Y")
st=input()
flag =0
if (int(st[0])+int(st[1]))%2 ==0:
    if (int(st[3])+int(st[4]))%2 ==0:
        if (int(st[4])+int(st[5]))%2 ==0:
            if (int(st[7])+int(st[8]))%2 ==0:
                flag=1
if st[2] in a:
    flag =0
if flag :
    print("valid")
else:
    print("invalid")