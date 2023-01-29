q2
#https://www.hackerrank.com/test/md1hiktjtk/questions/79gndqnaq56
#!/bin/python3

import math
import os
import random
import re
import sys


import requests
import json
#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#

def getSumFromArrayDict(arr, key):
    tot = 0
    for i in arr:
        tot += int(i[key])
    return tot
def getSingleSideGoals(url, teamNum):
    
    response = json.loads(requests.get(url + "1").text)
    totalPages = response["total_pages"]
    
    goals = getSumFromArrayDict(response["data"], teamNum)
    
    for i in range(2, totalPages+1):
        response = json.loads(requests.get(url + str(i)).text)
        goals += getSumFromArrayDict(response["data"], teamNum)
    return goals

def getWinner (competition, year):
    url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}"
    dct = json.loads(requests.get(url).text)
    return dct["data"][0]["winner"]

def getWinnerTotalGoals(competition, year):
    # Write your code here
    
    winner = getWinner(competition, year)
    url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}&page="
    homeGoals = getSingleSideGoals(url, "team1goals")
    
    url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={winner}&page="
    awayGoals = getSingleSideGoals(url, "team2goals")
    
    return homeGoals + awayGoals
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
