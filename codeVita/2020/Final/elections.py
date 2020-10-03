
n = int(input())
string = input()

nca=0
ncb=0
ca = 0
cb = 0
cd = 0
left = ""
right = ""


for i in range(n):
    
    if string[i] =='-':
        cd = cd + 1
    else:
        if string[i]=="A":
            nca = nca+1
        else:
            ncb = ncb+1
        left = right
        right = string[i]
        if left =="" and right =="A":
            ca = ca + cd
        elif left == "B" and right =="A" :
            ca = ca + cd//2
            cb = cb + cd//2
        elif left =="A" and right == "A":
            ca = ca + cd
        elif left == "B" and right =="B":
            cb = cb +cd
        cd = 0
    #print(f"str = {string[i]} left = {left} ri = {right} ca = {ca} cb = {cb} cd = {cd}")
if right =="B":
    cb = cb +cd

ca = ca + nca
cb = cb + ncb

#print(f"lef = {left}a={ca} b={cb}")

if cb>ca:
    print("B")
elif ca>cb:
    print("A")
else:
    print("Coalition government")
