

def prime_no(n):
    pl=[2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    pll=17
    c=0
    m=1
    for i in range(pll):
        if n==1:
            break
        m=m*pl[i]
        if m<=n:
            c+=1
        else:
            break
    return c

def prime_mult(n):
    pl=[1, 2, 6, 24, 120, 840, 9240, 120120, 2042040, 38798760, 892371480, 25878772920, 802241960520, 29682952539240, 1217001054108840, 52331045326680120, 2459559130353965640,2459559130353965640*53]
    pll=18
    c=0
    for i in range(pll):
        if pl[i]<=n:
            c+=1
        else:
            c-=1
            break

    return c
