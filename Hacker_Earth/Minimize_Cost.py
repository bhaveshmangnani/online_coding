n,k=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]

neg=0





for i in range(n):

    if lst[i]<0:
        neg=i
        break


start=max(0,neg-k)
end=min(n,neg+k)
print(f"start={start} end={end}")

s=sum(lst[0:end])+sum(lst[end:n])*-1
print(s)
