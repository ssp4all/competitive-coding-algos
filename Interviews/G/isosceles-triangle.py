# https://leetcode.com/discuss/interview-question/2255325/google-l4-onsite-june-2022

# A mountain can be simplified as an isoceles right triangle, whose base rests on the x-axis. 
# The two sides of the mountain are both at 45 degress to the base so the peak of the mountain forms a right angle.
# All the mountains are the same color so a mountian is invisible if its peak lies on 
# or within the triangular shape of any other mountain.
# Given a list of positions of all the mountain's peaks (x-y coordinates). Output the number of visible mountains.

# Example:

# Input:

# (4, 6)
# (7, 2)
# (2, 5)
# Output: 2

# here the peak visible are 1 and 3

# TC: O(NlgN)
# SC: O(N)

def visible(mtns: list) -> int:
    n = len(mtns)
    end, count = float('-inf'), 0
    for l, r in sorted([(y - x, y + x) for x, y in mtns]):
        if r > end:
            count += 1 
            end = r 
    return count 
    


