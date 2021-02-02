#URL: https://www.hackerrank.com/contests/foxtradingsolutions-internship-assessment/challenges/missing-stock-prices/submissions

import numpy as np
from scipy import interpolate

N = int(input())
prices = []
for i in range(N):
    date_time, price = input().split("\t")
    prices.append(price)


x_known = []
prices_float = []
x_unknown = []
#print("f",prices[6])
for i in range(N):
    if prices[i][0]!="M" and prices[i][0]!="m":
        x_known.append(i)
        prices_float.append(float(prices[i]))
    else:
        x_unknown.append(i)
        
prices_known = np.array(prices_float)
pred_model = interpolate.UnivariateSpline(x_known, prices_known, s=1)

for i in x_unknown:
    print(pred_model(i))
