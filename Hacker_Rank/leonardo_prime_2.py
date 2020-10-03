pl=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
pll=17

for _ in range(int(input())):

    n=int(input())
    c=0
    m=1
    for i in range(pll):
        if n==1:
            break
        m=m*pl[i]
        print(m)
        if m<=n:
            c+=1
        else:
            break
    print(c)
