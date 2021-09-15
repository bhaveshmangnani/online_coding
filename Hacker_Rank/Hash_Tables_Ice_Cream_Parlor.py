#URL: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def whatFlavors(n, cost, money):
    # Write your code here
    cost_set = set(cost)
    ele = 0
    first = second = 0
    for i in range(n):
        ele = money-cost[i]
        if ele in cost_set:
            if ele not in set(cost[i+1:]):
                continue
            first = i+1
            break
    
    for i in range(first, n):
        if cost[i] == ele:
            second = i+1
            break
    
    print(first, second)
