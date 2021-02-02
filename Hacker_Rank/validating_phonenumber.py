#URL: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
for _ in range(int(input())):
    print("YES" if re.search(r"^[789]{1}[0-9]{9}$",input()) else "NO"   )
