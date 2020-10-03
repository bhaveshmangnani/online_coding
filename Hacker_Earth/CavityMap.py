#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(n, a):
    s=[]
    s.append("".join(a[0]))
    for  i in range(1,n-1):
        t=str(a[i][0])
        for j in range(1,n-1):
            c=a[i][j]
            if c>a[i-1][j] and c>a[i+1][j] and c>a[i][j-1] and c>a[i][j+1]:
                t+="X"
            else:
                t=t+str(a[i][j])
        t=t+a[i][-1]
        s.append(t)
    s.append("".join(a[-1]))
    return s
                

    



from random import randint
n=randint(4,10)
s=[]
for i in range(n):
    t=""
    for j in range(n):
        t=t+str(randint(1,9))
    s.append(t)
print("Original-->")
print(n)
print("\n".join(s))
print("-"*20)
print("\n".join(cavityMap(n,s)))
