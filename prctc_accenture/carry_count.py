
num1 = input("n1: ")
num2 = input("n2: ")
n1 = len(num1)
n2 = len(num2)
en1 = num1[::-1]
en2 = num2[::-1]
mn = min(n1,n2)
carry=0
cnt = 0

for i in range(mn):
    c1 = int(en1[i])
    c2 = int(en2[i])
    s = c1 + c2 + carry
    carry = s//10
    if carry:
        cnt+=1
for i in range(mn, n1):
    c1 = int(en1[i])
    s = c1 + carry
    carry = s//10
    if carry:
        cnt+=1

for i in range(mn, n2):
    c2 = int(en2[i])
    s = c2 + carry
    carry = s//10
    if carry:
        cnt+=1


print(cnt)
