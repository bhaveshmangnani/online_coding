''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT



def main():
    n,r = map(int, input().split())
    
    graph = []
    
    src_sets = set()
    des_sets = set()
    costs = {}

    for i in range(r):
        
        src, des, cost = map(int, input().split())
        src_sets.add(src)
        des_sets.add(des)

        if des ==n:
            costs[src] = cost
    
    keys = costs.keys()
    for key in keys:
        if not ( (key in src_sets) and (des_sets) ):
            costs.pop(key)
    
    if costs:
        print(min(costs.values()), end = "")
    else:
        print("NOT POSSIBLE", end="")

        
main()
