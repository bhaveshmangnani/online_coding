#URL: https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

def stepPerms(n):
    # Write your code here
    if n==1 or n == 2:
        return n
    if n==3:
        return 4
    n_1 = 1
    n_2 = 2
    n_3 = 4
    newn = 0
    for i in range(3,n):
        newn = n_1 + n_2 + n_3
        n_1 = n_2
        n_2 = n_3
        n_3 = newn
    return n_3
