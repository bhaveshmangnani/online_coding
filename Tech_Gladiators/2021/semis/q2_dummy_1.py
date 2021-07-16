''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT




def main():
    n,r = map(int, input().split())
    
    graph = []
    src_set = set()
    des_set = set()

    costs = {}

    for i in range(r):
        item = list( map(int, input().split()) )

        src_set.add(item[0])
        des_set.add(item[1])

        if item[1]==n:
            costs[item[0]]= item[2]
    #print(costs)    
    keys = list(costs.keys())
    for key in keys:
        if key not in src_set:
            costs.pop(key)
    
    if costs:
        print(min(costs.values()), end= "" )
    else:
        print("NOT POSSIBLE", end= "")

        
main()
