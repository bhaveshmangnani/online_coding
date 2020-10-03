n = int(input())

bitlst = []

numlst = input().split()

for i in numlst:
  bitlst.append(str((int(min(i))*7 + int(max(i))*11)%100))
numlst = [int(x) for x in numlst]

tot = 0
cnt={}
for i in range(0,10):
  cnt[str(i)] = 0

for i in range(n):
    mb = bitlst[i][0]
    if cnt[mb]<2:
        for j in range(i+2,n,2):
            if cnt[mb]<2:
                if bitlst[j][0]==mb:
                    cnt[mb]+=1
                    tot +=1
            else:
                break
    else:
        continue

print(tot)
