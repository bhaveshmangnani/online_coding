n=int(input())
daimeter_hole=[int(x) for x in input().split()]

daimeter_hole=daimeter_hole[::-1]
m=int(input())

count=[]
position=[]

for i in range(m):
    position.append(0)

ball_index=n-1


for i in range(n):
    count.append(0)


daimeter_ball=[int(x) for x in input().split()]
print(f"dai_hole={daimeter_hole} dai_ball={daimeter_ball}")

for j in range(m):
    print(j)
    if daimeter_ball[j]<=daimeter_hole[ball_index]:
        if count[ball_index]<ball_index:
            count[ball_index]+=1
            position[j]=ball_index
        else:
            ball_index-=1
    else:
        ball_index-=1

print(position)
