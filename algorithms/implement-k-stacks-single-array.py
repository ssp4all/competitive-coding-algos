# https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/

#implement k stacks in one dammn array
"""
Create a data structure kStacks that represents k stacks.
 Implementation of kStacks should use only one array, i.e., 
 k stacks should use the same array for storing elements. 
 Following functions must be supported by kStacks.

push(int x, int sn) –> pushes x to stack number ‘sn’ where sn is from 0 to k-1
pop(int sn) –> pops an element from stack number ‘sn’ where sn is from 0 to k-1
"""

def KStacks(n, k):

    #initmazon
    stack = [0] * n
    next = [i for i in range(1, n + 1)]
    next[-1] = -1
    free = 0
    top = [-1] * n

    def is_empty(sn):
        return top[sn] == -1
    
    def is_full(sn):
        return free == -1

    def push(item, sn):
        nonlocal free

        if is_full(sn):
            return 
        
        position = free
        free = next[free]
        stack[position] = item
        next[position] = top[sn]
        top[sn] = position
        
    
    def pop(sn):
        nonlocal free
        if is_empty(sn):
            return
        position = top[sn]
        top[sn] = next[position]
        
        free = position
        return stack[position]
