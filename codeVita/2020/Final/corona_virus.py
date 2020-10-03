city = []
for i in range(9):
    city.append(list(input()))

city = city[::-1]

left = True
right = True

up = True
down = True
direction = 1
prev = 1

i = 0
j = 0

print(i,j)

for temp in range(20):
    if direction == 1:
        i = i + 1
        j = j + 1
    elif direction ==2:
        i = i + 1
        j = j - 1
    elif direction ==3:
        i = i -1
        j = j +1
    else:
        i = i-1
        j = j-1
    if city[i][j]=='a':
        if direction ==1: direction = 3
        elif direction ==2: direction = 1
        elif direction ==3: direction = 4
        elif direction ==4: direction = 2
    elif city[i][j]=='c':
        if direction ==1: direction = 2
        elif direction ==2: direction = 4
        elif direction ==3: direction = 1
        elif direction ==4: direction = 3
    elif city[i][j]=="*":
        print("i,j,left",i,j,left)
        if i ==0 and left:
            left = False
            if direction ==3: direction =1
            elif direction ==4: direction =2
        elif i==19 and right:
            right = False
            if direction ==1: direction =3
            elif direction ==2: direction =4
        elif j ==0 and down:
            down=False
            if direction ==2: direction =1
            elif direction ==4: direction =3
        elif j==19 and up:
            up = False
            if direction ==1: direction=2
            elif direction ==3: direction =4
        else:
            #print("")
            break
                

    print(f"l = {left} temp = {temp} p = {city[i][j]} dir = {direction} i,j",i,j)
    
