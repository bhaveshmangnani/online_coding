def acmTeam(topics):
    comb = combinations(topics,2)
    m = 0
    count = 0
    for i in comb:
        n = str(bin(((int(i[0],2) | int(i[1],2)))))[2:].count('1')
        if n > m:            
            m = n
            count = 1
        elif n == m:
            count += 1
    return (m, count)

input()
a=[int(x) for x in input().split()]
print(acmTeam(a))


