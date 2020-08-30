https://leetcode.com/problems/construct-string-from-binary-tree/

IP:  [1,2,3,null,4]
OP: "1(2()(4))(3)"

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        global ans
        ans = ""
       
        def preorder(root):
            global ans
            if not root:    return
            ans += str(root.val)
            if root.left or root.right:
                ans += "("
                preorder(root.left)
                ans += ")"
            if root.right:
                ans += "("   
                preorder(root.right)
                ans += ")"
            
        preorder(t)
        return ans