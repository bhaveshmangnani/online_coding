#URL: https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    tot = 0
    for i in prices:
        if i<k:
            k-=i
            tot+=1
    return tot
