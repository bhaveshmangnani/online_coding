n,k=[int(x) for x in input().split()]

ar=[int(x) for x in input().split()]
p=0

for i in range(n):
    
    for j in range(i+1,n):
        if not(abs(ar[i]-ar[j])-k):
            p+=1
            break
print(p)
