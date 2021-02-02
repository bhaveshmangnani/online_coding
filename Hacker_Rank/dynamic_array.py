#URL: https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    # Write your code here
    la = 0
    lst = []
    for _ in range(n):
        lst.append([])
    ans = []
    for t,x,y in queries:
        if t==1:
            index = (x^la) %n
            lst[index].append(y)
        else:
            index = (x^la) %n
            s = len(lst[index])
            la = lst[index][y%s]
            ans.append(la)
    return ans
