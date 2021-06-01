import math
def initial(a,k):
      return ((1-2*a)+math.sqrt(1-4*a+4*a*a+8*k))/2

def solve(k):
      count=0
      for i in range(1,k+1):
            if initial(i,k)-int(initial(i,k))==0:
                  #print(i)
                  count+=1
      return count

"""
for _ in range(int(input())):
      print("Case #{}:".format(_+1),end=" ")
      print(solve(int(input())))
"""
for q in range(1,1000000):
    #print(q,":",solve(q))
    nums = solve(q)
    sqt = int(math.sqrt(q))
    if nums>sqt:
        print(f"{q} -> {nums} {sqt}")
