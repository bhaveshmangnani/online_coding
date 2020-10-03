import sys


string1=input()
slen=len(string1)
dirlist=input().split()
n=int(dirlist[0])


if n<slen:
    print("NO")
    sys.exit(0)
dirlist.remove(dirlist[0])

indexList=[]
for i in range(0,2*n,2):


    if dirlist[i].lower()=='l':
        indexList.append(int(dirlist[i+1])%slen)
    else:
        indexList.append(-1*(int(dirlist[i+1])%slen))
    
    
print(indexList)

strdict={}
answer={}
for i in string1:
    strdict[i]=string1.count(i)
    answer[i]=0




for i in range(n):
    answer[string1[i]]+=1
    
    print(f"answer={answer}")

if strdict==answer:
    print("YES")
else:
    print("NO")
