#URL: https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
string = input()
ptn = input()
ptn = re.compile(ptn)
res = ptn.search(string)
if res:
    
    while res:
        s = res.start()
        print((s,res.end()-1))
        res = ptn.search(string,s+1)
else:
    print("(-1, -1)")
