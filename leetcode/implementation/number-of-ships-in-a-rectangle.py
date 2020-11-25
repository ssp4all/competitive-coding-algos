https://leetcode.com/problems/number-of-ships-in-a-rectangle/

"""
On the sea represented by a cartesian plane, each ship is located at 
an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two 
points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a 
rectangle, return the number of ships present in that rectangle.  
It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  
Also, any solutions that attempt to circumvent the judge will result in disqualification.

"""

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight, bottomLeft):  return 0
        
        
        c, d = topRight.x, topRight.y
        a, b = bottomLeft.x, bottomLeft.y

        if (c, d) == (a, b):    return 1
        
        mid_x = (c + a) // 2
        mid_y = (d + b) // 2
        
        return self.countShips(sea, Point(c, d), Point(mid_x + 1, mid_y + 1)) + \
                self.countShips(sea, Point(c, mid_y), Point(mid_x + 1, b)) + \
                self.countShips(sea, Point(mid_x, mid_y), Point(a, b)) + \
                self.countShips(sea, Point(mid_x, d), Point(a, mid_y + 1))
    