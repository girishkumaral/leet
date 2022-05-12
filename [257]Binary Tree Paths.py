# Given the root of a binary tree, return all root-to-leaf paths in any order. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: ["1"]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics String Backtracking Tree Depth-First Search Binary Tree 👍 405
# 5 👎 184


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        s = [(root, str(root.val))]
        paths = []
        while s:
            node, path = s.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                s.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                s.append((node.right, path + "->" + str(node.right.val)))
        return paths
# leetcode submit region end(Prohibit modification and deletion)

