''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def check_list(src, des, roadmap):
    if roadmap[src] ==[]:
        return False
    if des in roadmap[src]:
        return src
    for i in


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
            print("NOT POSSIBLE")
        else:
            check_list = roadmap[1]
            for i in check_list:
                cost = check_reach(i, n, roadmap)
        
main()''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def check_list(src, des, roadmap):
    if roadmap[src] ==[]:
        return False
    if des in roadmap[src]:
        return src
    for i in


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
            print("NOT POSSIBLE")
        else:
            check_list = roadmap[1]
            for i in check_list:
                cost = check_reach(i, n, roadmap)
        
main()''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def check_list(src, des, roadmap):
    if roadmap[src] ==[]:
        return False
    if des in roadmap[src]:
        return src
    for i in


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
            print("NOT POSSIBLE")
        else:
            check_list = roadmap[1]
            for i in check_list:
                cost = check_reach(i, n, roadmap)
        
main()''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def check_list(src, des, roadmap):
    if roadmap[src] ==[]:
        return False
    if des in roadmap[src]:
        return src
    for i in


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
            print("NOT POSSIBLE")
        else:
            check_list = roadmap[1]
            for i in check_list:
                cost = check_reach(i, n, roadmap)
        
main()''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

