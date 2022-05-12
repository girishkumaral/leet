# You are given two binary trees root1 and root2. 
# 
#  Imagine that when you put one of them to cover the other, some nodes of the 
# two trees are overlapped while the others are not. You need to merge the two 
# trees into a new binary tree. The merge rule is that if two nodes overlap, then sum 
# node values up as the new value of the merged node. Otherwise, the NOT null 
# node will be used as the node of the new tree. 
# 
#  Return the merged tree. 
# 
#  Note: The merging process must start from the root nodes of both trees. 
# 
#  
#  Example 1: 
# 
#  
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 2000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 65
# 22 👎 243


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if not root1 and root2:
            return root2

        if not root2 and root1:
            return root1

        Newroot = root1

        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val = node1.val+node2.val
            if node1.left and node2.left:
                stack.append((node1.left, node2.left))
            elif not node1.left and node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                stack.append((node1.right, node2.right))
            elif not node1.right and node2.right:
                node1.right = node2.right

        return Newroot
# leetcode submit region end(Prohibit modification and deletion)