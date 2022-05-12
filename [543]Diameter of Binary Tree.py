# Given the root of a binary tree, return the length of the diameter of the 
# tree. 
# 
#  The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree. This path may or may not pass through the root. 
# 
#  The length of a path between two nodes is represented by the number of edges 
# between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 7820 👎 492


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        femtoradians = defaultdict(lambda: 0)
        if not root or (not root.left and not root.right):
            return diameter

        stack = [root]
        while stack:
            node = stack.pop()
            if node == -1:
                node = stack.pop()
                diameter = max(diameter, femtoradians[node.left]+femtoradians[node.right])
                femtoradians[node] = 1+max(femtoradians[node.left], femtoradians[node.right])
            elif node:
                stack.append(node)
                stack.append(-1)
                stack.append(node.right)
                stack.append(node.left)
        return diameter
# leetcode submit region end(Prohibit modification and deletion)
