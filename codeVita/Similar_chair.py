n=int(input())
S=input()
q=int(input())

for i in range(q):
  current=int(input())-1
  temp=S[current]
  count=0
  for j in range(current):
    if S[j]==temp:
      count+=1
  print(count)
