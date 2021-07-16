

def check_limit(src, des, graph):
    element = graph[src][des]
    if element!=0:
        graph[src][des] = [element, True]
        #return graph

    for i in range(des+1):
        if graph[src][i]!=0:
            graph = check_limit(i, des, graph)
    return graph


def main():
    n,r = map(int, input().split())
    
    graph = []
    for _ in range(n):
        graph.append([0]*n)
    for i in range(r):
        
        src, des, cost = map(int, input().split())
        graph[src-1][des-1] = cost

    graph = check_limit(0, n-1, graph)
    costs = []
    for i in range(n):
        if type(graph[i][n-1]) == list:
            costs.append(graph[i][n-1][0])
    if costs:
        print(min(costs))
    else:
        print("NOT POSSIBLE")
main()
