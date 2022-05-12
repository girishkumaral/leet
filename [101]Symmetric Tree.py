# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively? Related 
# Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 9352 👎 231


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        s = [(root.left, root.right)]
        while s:
            i, j = s.pop()
            if i or j:
                if (i and not j) or (j and not i) or (i.val != j.val):
                    return False
                s.append((i.left, j.right))
                s.append((i.right, j.left))
        return True
# leetcode submit region end(Prohibit modification and deletion)
