
def check_reach(src, des, roadmap):
    if roadmap[src] ==[]:
        return False
    if des in roadmap[src]:
        return src
    for i in roadmap[src]:
        return check_reach(i, des, roadmap)


def generatemap(graph,n):
    
    roadmap = {}

    for i in range(n):
        roadmap[i+1] = []

    costs = {}
    for src, des, cost in graph:
        if des == n :
            costs[src] = cost
        roadmap[src].append(des)
    return roadmap, costs


def main():
    n,r = map(int, input().split())
    
    graph = []
    
    is_des = False
   
    for i in range(r):
        
        item = list(map(int, input().split()))
        graph.append(item)
        if (not is_des) and (item[1]==n):
            is_des = True 
    if not is_des:
        print("NOT POSSIBLE", end = "")
    else:
        roadmap, costs = generatemap(graph,n)
        if roadmap[1] ==[]:
            print("NOT POSSIBLE",end="")
        else:
            check_list = roadmap[1]
            pre_final = []
            for i in check_list:
                pf = check_reach(i, n, roadmap)
                if pf!=False:
                    pre_final.append(pf)
            if pre_final:
                mincost = costs[pre_final[0]]
                for lastele in pre_final:
                    mincost = min(mincost, costs[lastele])
                print(mincost,end="")
            else:
                print("NOT POSSIBLE",end = "")
main()
