#URL:https://www.hackerrank.com/challenges/matrix-script/problem
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
matrix ="".join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print( re.sub( r"\b[^0-9a-zA-Z]+\b"," ",matrix ) )
