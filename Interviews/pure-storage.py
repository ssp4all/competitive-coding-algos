class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def print_singly_linked_list(head):
    tmp = head
    while tmp != None:
        print(tmp.val, end=' ')
        tmp = tmp.next_node

def add_to_singly_linked_list(head, val):
    tmp = head
    while tmp.next_node != None:
        tmp = tmp.next_node
    tmp.next_node = Node(val)

"""
For your reference, here's the node structure:
class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node
"""

def remove_all_n(head, n):
    # Fill in the logic here
    if not head:    return
    
    while head and head.val == n:
        head = head.next_node
    cur = head
    prev = head
    while cur:
        if cur.val == n:
            prev.next_node = cur.next_node
            cur = cur.next_node
        else:
            prev = cur
            cur = cur.next_node
            
    # if cur
    return head

def main():


#!/bin/python3

import math
import os
import random
import re
import sys


# Preconditions:
#    array is sorted, smallest to largest, without duplicates

def countPairs(array, diff):
    """
    Returns the number of pairs in array that differ by diff.
    See problem statement for description of algorithm.
    array: list of unique integers
    diff: integer, the targeted difference
    return: number of pairs realizing the difference
    """
    pairs = 0
    n = len(array)
    i, j = 0, 1
    print("->", array)
    while j < n:
        for j in range(j, n):
            if array[j] - array[i] == diff:
                pairs += 1
                break
                # print(array[j], array[i])
        i += 1
        j = i + 1

    return pairs

if __name__ == '__main__':