#!/bin/python3

import math
import os
import random
import re
import sys


import requests
import json

def getArticleTitles(author):
    # Write your code here
    if not author:  return []
    url = "https://jsonmock.hackerrank.com/api/articles?author={0}".format(author)
    # print(url)
    response = requests.get(url)
    res = json.loads(response.content)
    titles = []
    # print(res['data'])
    # for 
    for t in res['data']:
        if not t['title'] and not t['story_title']:
            continue
        elif not t['title']:
            titles += [t['story_title']]
        else:
            titles += [t['title']]

    return titles

if __name__ == '__main__':



----------------
def maxDifference(px):
    # Write your code here
    if not px:  return -1
    n = len(px)
    ans = -1
    for i in range(1, n):
        temp = i - 1
        while temp > -1 and px[temp] < px[i]:
            ans = max(ans, px[i] - px[temp])
            temp -= 1
    return ans


------------------------
SELECT 
    (SCORE) 
FROM STUDENT 
    ORDER BY 
    SCORE 
    DESC 
limit 213,1; 
