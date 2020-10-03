f = open("travel_restrictions_validation_input.txt",'r')
try:
    t = int(f.readline())
    print(t)
    for i in range(t):
        n = int(f.readline())
        inc = f.readline()[:n]
        out = f.readline()[:n]
        print(n)
        print(inc)
        print(out)
finally:
    f.close()
