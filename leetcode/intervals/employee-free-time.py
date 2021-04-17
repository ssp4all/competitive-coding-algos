https://leetcode.com/problems/employee-free-time/

"""
We are given a list schedule of employees, which represents 
the working time for each employee.

Each employee has a list of non-overlapping Intervals, 
and these intervals are in sorted order.

Return the list of finite intervals representing common, 
positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form 
[x, y], the objects inside are Intervals, not lists or 
arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, 
and schedule[0][0][0] is not defined).  Also, we wouldn't include 
intervals like [5, 5] in our answer, as they have zero length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
"""


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

#TC:O(NlgN), SC:O(2*N)

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        events = []
        for emp in schedule:
            for int in emp:
                events += [[int.start, 1]]
                events += [[int.end, -1]]
            
        events.sort() 
        
        prev = None
        bal = 0 
        
        free = []
        for time, type in events:
            if bal == 0 and prev:
                if prev != time:
                    free += [Interval(prev, time)]
            
            bal += type 
            prev = time 
        
        return free