#URL:https://www.hackerrank.com/challenges/validating-credit-card-number/problem

def is_valid(num):
    
    f = num[0]
    if f!="4" and f!="5" and f!="6":
        return False
    num = num.split("-")
    for n in num:
        l = len(n)
        if l!=4 and l!=16:
            return False
    num = "".join( num )
    if len(num)!=16:
        return False
    if not num.isdecimal():
        return False
    
    for i in range(3,16):
        if num[i]==num[i-1] and num[i]==num[i-2] and num[i]==num[i-3]:
            return False
    return True



for _ in range(int(input())):
    if is_valid( input() ):
        print("Valid")
    else:
        print("Invalid")
