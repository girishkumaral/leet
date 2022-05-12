# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 69
# 48 👎 124


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from  collections import defaultdict
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        nodetodepth = defaultdict(lambda: 0)

        stack.append(root)
        while stack:
            node = stack.pop()
            if node == -1:
                node = stack.pop()
                nodetodepth[node] = 1+max(nodetodepth[node.left], nodetodepth[node.right])
            elif node:
                stack.append(node)
                stack.append(-1)
                stack.append(node.right)
                stack.append(node.left)
        return nodetodepth[root]
# leetcode submit region end(Prohibit modification and deletion)
