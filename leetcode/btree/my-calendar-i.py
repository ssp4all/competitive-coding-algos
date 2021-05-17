https://leetcode.com/problems/my-calendar-i/

"""
Implement a MyCalendar class to store your events. A new event can be
 added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, 
this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection 
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event 
can be added to the calendar successfully without causing a double booking. 
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); 
MyCalendar.book(start, end)
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

############################################################

https://leetcode.com/problems/my-calendar-ii/

""" 
Implement a MyCalendarTwo class to store your events. 
A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). 
Formally, this represents a booking on the half open interval 
[start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty 
intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event 
can be added to the calendar successfully without causing a triple booking. 
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); 
MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
"""

class MyCalendarTwo:

    def __init__(self):
        self.calender = []  #one bookings
        self.overlaps = [] #double bookings
        
    #TC: O(N^2)
    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return 0 
        
        #not a double booking 
        for i, j in self.calender:
            if start < j and end > i:
                self.overlaps += [(max(start, i), min(end, j))]
            
        self.calender += [(start, end)]
            
        return 1

############################################################


https://leetcode.com/problems/my-calendar-iii/submissions/
"""
A k-booking happens when k events have some non-empty intersection 
(i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, 
return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the 
largest integer such that there exists a k-booking in the calendar.
 
Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]
"""

# TC:O(B*NlgN), SC:O(B)
class MyCalendarThree:

    def __init__(self):
        self.calender = Counter()

    def book(self, start: int, end: int) -> int:
        self.calender[start] += 1 
        self.calender[end] -= 1 
        
        active = ans = 0 
        for x in sorted(self.calender):
            active += self.calender[x]
            ans = max(ans, active)
        
        return ans

# TC:O(B*N), SC:O(N)
class MyCalendarThree(object):
    def __init__(self):
        self.pos = []
        self.delta = {}
        self.max = 0

    def book(self, start, end):
        i = bisect.bisect_left(self.pos, start)
        if start not in self.delta:
            self.delta[start] = self.delta[self.pos[i-1]] if i else 0
            self.pos[i:i] = [start]

        j = bisect.bisect_left(self.pos, end)
        if end not in self.delta:
            self.delta[end] = self.delta[self.pos[j-1]]
            self.pos[j:j] = [end]
        
        for k in range(i, j):
            self.delta[self.pos[k]] = c = self.delta[self.pos[k]] + 1
            self.max = max(self.max, c)
        # print(i, j, self.pos, self.delta)
        return self.max
        