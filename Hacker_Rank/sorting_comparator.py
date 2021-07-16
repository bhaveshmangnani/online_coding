#URL: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return name+str(score)
    def comparator(a, b):
        res = -a.score + b.score
        if res!=0:
            return res
        else:
            if a.name>b.name: 
                return 1
            return -1
