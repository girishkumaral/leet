# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
# 
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 56
# 61 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        s = [(p, q)]
        while s:
            i, j = s.pop()
            if (i and not j) or (j and not i):
                return False
            if i and j:
                if i.val != j.val:
                    return False
                s.append((i.right, j.right))
                s.append((i.left, j.left))
        return True


# leetcode submit region end(Prohibit modification and deletion)
