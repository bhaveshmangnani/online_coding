#https://www.hackerrank.com/challenges/funny-string
def funnyString(s):
    
    n = len(s)
    for i in range(n//2):
        left = i
        right = n-i-1
        if abs(ord(s[left]) - ord(s[left + 1])) != abs(ord(s[right]) - ord(s[right - 1])):
            return "Not Funny"
    return "Funny"
