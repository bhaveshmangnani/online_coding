from collections import Counter
def happyLadybugs(lb,b):
    s=set(b)
    if "_" in s:
        ls=tuple(s)
        dct = dict(Counter(b))
        for i in ls:
            if i!="_" and dct[i]==1:
                return "NO"
        return "YES"

    else:
        f=True
        for i in range(1,lb-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                f=False
                break
        if f:
            if b[-1]!=b[-2]:
                return "NO"
            return "YES"
        return"NO"
lst=list(range(26))
start=ord('A')
cl=[]
for i in lst:
    cl.append(chr(i+start))

cl.append("_")
for _ in range(5):
    import random
    n = random.randint(5,10)
    t = ""
    for i in range(n):
        t=t+cl[random.randint(0,26)]
    print(n)
    print(t)
    print(happyLadybugs(n,t))
