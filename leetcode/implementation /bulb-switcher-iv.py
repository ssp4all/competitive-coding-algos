https://leetcode.com/problems/bulb-switcher-iv

"""
There is a room with n bulbs, numbered from 0 to n-1, arranged in a row from left to right. 
Initially all the bulbs are turned off.

Your task is to obtain the configuration represented by target where target[i] is '1' if the 
i-th bulb is turned on and is '0' if it is turned off.

You have a switch to flip the state of the bulb, a flip operation is defined as follows:

Choose any bulb (index i) of your current configuration.
Flip each bulb from index i to n-1.
When any bulb is flipped it means that if it is 0 it changes to 1 and if it is 1 it changes to 0.

Return the minimum number of flips required to form target.


"""
class Solution:
    def minFlips(self, target: str) -> int:
        if "0"*len(target) == target:  return 0
        
        
        flips, status = 0, "0"
        n = len(target)
        for i in range(n):
            if target[i] != status:
                status = "1" if status == "0" else "0"
                flips += 1
        return flips