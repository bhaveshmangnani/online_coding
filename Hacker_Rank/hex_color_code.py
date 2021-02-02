#URL: https://www.hackerrank.com/challenges/hex-color-code/problem

import re

for _ in range( int(input()) ):
    line = input()
    ans = re.findall( r"[\s:]((\#([a-f0-9]{3}){1,2}))", line,re.I )
    #print(ans)
    for i in ans:
        print(i[0])
