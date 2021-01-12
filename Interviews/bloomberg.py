'''
                World
              /   |   \
             /    |    \
            C     A     B
          / |     |    /|\
         /  |     |   / | \
        E   D     F  H  G  I
        
            World
          /   |   \
         /    |    \
        A     B     C
        |    /|\    |\
        |   / | \   | \
        F  G  H  I  D  E

        '''
class Node:
    def __init__(self, val:char)->None:
        self.key = val 
        self.children = []

class Solution:
    # def sfd
    def sort_tree(root : 'Node')->'Node':
        if not root: return root 
  
        def dfs(node):
            if not node.children or not node:    return node 
            for child in node.children:
                dfs(child)
            node.children.sort(key=lambda child: child.key)
            return node
                
        dfs(root)
                
Q 2 
    """
given sorted array by its mod values then sort it actually (less than NlgN)
-1, 2, -4, 0,5, 6, -10, -13, -22 -> -22, -13, -10, -4, -1,0, 2, 5, 6

-1,-4,-10 -13 -22
[-22, -13, -10, -4, -1], [0, 2, 5, 6]

|-1| = 1
|2| = 2

[4, 1, 2, 3]
"""

def sort_abs_values(arr: list)->list: #not in place
    if not arr: return arr 
        
    negatives = []
    positives = []
    for val in arr:
        if val < 0:
            negatives += [val]
        else:
            positives += [val]        
    
    return negatives[::-1] + positives

Q 3. given 2d matrix, find maximum path sum in given N steps

 2, 3, 4, 6
 1, 2, 3 ,5
 3, 4, x ,5
 0, 1, 2, 3
N = 2

 starting cordinate = (2,2)
N = 2
Output: 10 5->5
    