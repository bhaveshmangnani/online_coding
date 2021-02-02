#URL: https://www.hackerrank.com/challenges/re-group-groups/problem

import re
ans = re.search(r"([a-zA-Z0-9])\1+",input())
print(ans.group(1) if ans else -1 )
