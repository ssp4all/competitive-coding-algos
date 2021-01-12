https://leetcode.com/problems/my-calendar-i/

"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
"""

# simulate TreeMap of Java in pYthon

class Node:
    def __init__(self, start, end):
        self.start = start 
        self.end = end 
        self.left = self.right = None 

class BSTree:
    def __init__(self, start, end):
        self.root = Node(start, end)

    # O(lgH)
    def insert(self, node, cur):
        if node.start >= cur.end:
            if not cur.right:
                cur.right = node 
                return 1 
            return self.insert(node, cur.right)
        elif node.end <= cur.start:
            if not cur.left:
                cur.left = node
                return 1 
            return self.insert(node, cur.left)
        return 0 
    
class MyCalendar:

    def __init__(self):
        self.tree = None
        
    def book(self, start: int, end: int) -> bool:
        if not self.tree:
            self.tree = BSTree(start, end)
            return 1
        return self.tree.insert(Node(start, end), self.tree.root)
        