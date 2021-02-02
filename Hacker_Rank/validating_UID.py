#URL: https://www.hackerrank.com/challenges/validating-uid/problem

import re
def is_valid(UID):
    #ptn = r"A-Z]{2,}"
    #print("check",re.search( ptn,UID ))
    if not (re.search( r"^[0-9a-zA-Z]{10}$",UID ) and\
     re.search( r".*[A-Z].*[A-Z]",UID ) and\
     re.search( r"(.*[0-9].*){3}",UID ) and\
      not re.search(r".*(.).*\1",UID)):
        return "Invalid"
    return "Valid"
    

for _ in range(int(input())):
    print(is_valid(input()))
