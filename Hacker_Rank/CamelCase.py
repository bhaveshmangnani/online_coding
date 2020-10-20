#URL: https://www.hackerrank.com/challenges/camelcase/problem?h_r=profile

def camelcase(s):
    cnt  = 1
    for ch in s:
        if ch>="A" and ch<="Z":
            cnt+=1
    return cnt
