from math import *
import sys

def sum_list(x):
    if x==0:
        return 3
    
    tempsum=0
    for i in range(x):
        tempsum=tempsum+3*(2**i)
    return tempsum


n=int(input())
if n==1:
    print(3)
    sys.exit(0)
x=int(log(n/3)/log(2))

disp=n-sum_list(x)-1
if x:
    print(3*(2**x) - disp)
else:
    print(3*(2**(x+1))-disp)
