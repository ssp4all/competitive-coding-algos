https://leetcode.com/problems/count-unhappy-friends/

"""
You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. 
In other words, a friend earlier in the list is more preferred than a friend later in the list. 
Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, 
where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy.
 A friend x is unhappy if x is paired with y and there exists a 
 friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.
"""

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mapping = {}
        
        for i, j in pairs:
            mapping[i] = preferences[i][:preferences[i].index(j)]
            mapping[j] = preferences[j][:preferences[j].index(i)]

        ans = 0
        
        for key in mapping:
            for pref in mapping[key]:
                if key in mapping[pref]:
                    ans += 1
                    break
        return ans