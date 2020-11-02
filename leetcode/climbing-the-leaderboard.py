https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

"""
An arcade game player wants to climb to the top of the leaderboard and track 
their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the 
next player(s) receive the immediately following ranking number.
Example


The ranked players will have ranks , , , and , respectively. If the player's 
scores are ,  and , their rankings after each game are ,  and . Return .
"""


def climbingLeaderboard(ranked, player):
    rankings = [1]
    ans = []
    n = len(ranked)
    for i in range(1, n):
        if ranked[i] < ranked[i - 1]:
            rankings += [rankings[-1] + 1]
        else:
            rankings += [rankings[-1]]

    ptr = n - 1
    for p in player:
        while ptr >= 0 and p > ranked[ptr]:
            ptr -= 1
        
        if ranked[ptr] == p:
            ans += [rankings[ptr]]
        elif ranked[ptr] < p:
            ans += [1]
        else:
            ans += [rankings[ptr] + 1]
    
    return ans
