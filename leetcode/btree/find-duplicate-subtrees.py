https://leetcode.com/problems/find-duplicate-subtrees/

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root: return 
        ans = []
        subtrees = set()
        def helper(root):
            if not root:    return
            temp = []
            def preorder(root):
                if not root:    return
                temp.append(root.val)
                if root.left:
                    preorder(root.left)
                if root.right:
                    preorder(root.right)
            preorder(root)
            if temp and tuple(temp) in subtrees \
                and temp not in ans:
                ans.append(temp)
            else:
                subtrees.add(tuple(temp))
            helper(root.left)
            helper(root.right)   
        helper(root.left)
        helper(root.right)
        print(ans)
        return []
IP: [1,2,2,3,7,3,7,8,4,null,null,8,4]
OP: [[2, 3, 8, 4, 7], [3, 8, 4], [8], [4], [7]]

Optimized

from collections import Counter
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:    return root
        count = Counter()
        ans = []
        
        def helper(node):
            if not node: return "#"
            serial = f"{node.val}{helper(node.left)}{helper(node.right)}"
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial
       
        helper(root)
        print(count)   
        return ans
