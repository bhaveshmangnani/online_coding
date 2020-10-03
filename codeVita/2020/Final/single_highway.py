#import math

n = int(input())
ar = [int(x) for x in input().split()]

#f = math.factorial(n)
s = 0.0

for i in range(1,n+1):
    s = s + 1/i
print("%.6f"%s)
