#https://www.hackerrank.com/test/md1hiktjtk/questions/32gbiihfdea
#!/bin/python3

import math
import os
import random
import re
import sys


import requests
import json

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getSumFromArrayDict(arr, key):
    tot = 0
    for i in arr:
        tot += int(i[key])
    return tot

def getSingleSideGoals(team, url, teamNum):
    
    response = json.loads(requests.get(url + "1").text)
    totalPages = response["total_pages"]
    
    goals = getSumFromArrayDict(response["data"], teamNum)
    
    for i in range(2, totalPages+1):
        response = json.loads(requests.get(url + str(i)).text)
        goals += getSumFromArrayDict(response["data"], teamNum)
    return goals
    
    
    

def getTotalGoals(team, year):
    # Write your code here
    
    url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page="
    homeGoals = getSingleSideGoals(team, url, "team1goals")
    
    url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page="
    awayGoals = getSingleSideGoals(team, url, "team2goals")
    
    return homeGoals + awayGoals
    
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
