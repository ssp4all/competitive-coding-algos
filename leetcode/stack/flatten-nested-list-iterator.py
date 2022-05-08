https://leetcode.com/problems/flatten-nested-list-iterator

"""
You are given a nested list of integers nestedList. 
Each element is either an integer or a list whose 
elements may also be integers or other lists. 
Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes 
the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some 
integers in the nested list and false otherwise.
 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

"""

class NestedIterator(object):

    def __init__(self, nestedList):
        self.st = [[nestedList, 0]]

    def next(self):
        self.hasNext() #already getting called before next()
        li, idx = self.st[-1]
        self.st[-1][1] += 1
        return li[idx].getInteger()

    def hasNext(self):
        while self.st:
            li, idx = self.st[-1]
            if (idx == len(li)):
                self.st.pop()
            else:
                if li[idx].isInteger():
                    return 1 
                self.st[-1][1] += 1
                self.st += [[li[idx].getList(), 0]]
        return 0       