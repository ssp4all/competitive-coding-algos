https://leetcode.com/problems/reconstruct-itinerary

"""
Given a list of airline tickets represented by pairs of departure and arrival airports 
[from, to], reconstruct the itinerary in order. All of the tickets belong to a man who 
departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the
 smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] 
 has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel = defaultdict(list)
        
        for i, j in sorted(tickets, reverse=1):
            travel[i] += [j]
        
        s = ["JFK"]
        ans = []
        while s:
            while travel[s[-1]]:
                dest = travel[s[-1]].pop()
                s += [dest]
            ans += [s.pop()]
            
        return ans[::-1]