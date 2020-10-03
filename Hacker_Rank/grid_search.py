# search based solution  
for _ in range(int(input())):
    big = []
    small = []
    R, C = map(int, input().split())
    for __ in range(R):
        big.append(input())
    big_str = "".join(big)
    r, c = map(int, input().split())
    for __ in range(r):
        small.append(input())
    small_str = small[0]
    # get all starting positions of first line of small grid
    t = [i for i in range(len(big_str)) if big_str.startswith(small_str, i)]
    print("t=",t)
    for i in t:
        flag = 1
        row = i / C
        col = i % C
        if row > R - r:
            flag = 0
            continue
        for j in range(1,r):
            if small[j] != big[row+j][col: col + c]:
                flag = 0
                break
        if flag == 1:
            print("YES")
            break
    else:
        print("NO")
