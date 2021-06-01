#URL: https://www.hackerrank.com/challenges/waiter/problem
def waiter(n, number, q):
    #
    # Write your code here.
    #
    
    def prime_list(n):
        import math
        ans = []
        cnt = 0
        i = 2
        while cnt<n:
            flag = True
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j ==0:
                    flag = False
                    break
            if flag:
                cnt += 1
                ans.append(i)
            i+=1
        return ans
    
    pl = prime_list(q)
    ans = []
    a=number
    
    for i in range(q):
        
        for j in range(n):
            if a[j] and (a[j]%pl[i]==0):
                ans.append(a[j])
                a[j] = 0
        b=[]
        a=a[::-1]
    ans += [ n for n in a[::-1] if n ]
    return ans
