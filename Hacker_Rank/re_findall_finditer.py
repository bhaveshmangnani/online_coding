#URL: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re
v = 'aeiou'
c = 'bcdfghjklmnpqrstvwxyz'
ans = re.findall("(?=[%s]([%s]{2,})[%s])"%(c,v,c),input(),re.I)
print(*ans or [-1],sep="\n")
