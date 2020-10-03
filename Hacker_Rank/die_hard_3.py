def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def solve(a, b, c):
    if a<c and b<c:
        return "NO"
    if gcd(a,b)==1:
        return "YES"
    if a==c or b==c:
        return"YES"
    if c%a==0 or c%b==0:
        return "YES"
    return "NO"
import random
t=random.randint(1,12)
for i in range(t):
    a = random.randint(1,20)
    b = random.randint(1,20)
    c = random.randint(1,20)
    print(a,b,c)
    print(solve(a,b,c))
