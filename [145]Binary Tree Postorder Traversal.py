# Given the root of a binary tree, return the postorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,3]
# Output: [3,2,1]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively? 
# Related Topics Stack Tree Depth-First Search Binary Tree 👍 4138 👎 141


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [0]
        if not root:
            return []
        postorder = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node == -1:
                node = stack.pop()
                postorder.append(node.val)
            elif node:
                stack.append(node)
                stack.append(-1)
                stack.append(node.right)
                stack.append(node.left)
        return postorder
# leetcode submit region end(Prohibit modification and deletion)
