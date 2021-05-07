https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        # n = len(nums)
        # mid = nums[n//2]
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # print(root)
        return root


class Solution:
    def sortedArrayToBST(self, nums: List[int], l=0, r=float('inf')) -> TreeNode:
        if not nums: return None
        if  r == float('inf'): 
            r = len(nums)-1
        if l <= r:
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums, l, mid-1)
            root.right = self.sortedArrayToBST(nums, mid+1, r)
            return root
        return None
        

#this one is for a Sorted Linked List
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:    return None 
        
        def helper(head, tail):
            if not head:    return head 
            
            slow, fast = head, head 
            if head == tail:    return None 
            
            # find middle
            while fast != tail and fast.next != tail:
                slow, fast = slow.next, fast.next.next
            
            root = TreeNode(slow.val)
            root.left = helper(head, slow)
            root.right = helper(slow.next, tail)
            return root 
    
        return helper(head, None)