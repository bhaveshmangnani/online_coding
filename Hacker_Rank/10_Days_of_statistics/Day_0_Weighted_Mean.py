#URL: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

def weightedMean(n, X, W):
    # Write your code here
    xw_sum=0
    w_sum=0
    for i in range(n):
        xw_sum += X[i]*W[i]
        w_sum += W[i]
    print(round(xw_sum/w_sum,1))
