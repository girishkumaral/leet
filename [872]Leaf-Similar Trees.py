# Consider all the leaves of a binary tree, from left to right order, the 
# values of those leaves form a leaf value sequence. 
# 
#  
# 
#  For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
#  8). 
# 
#  Two binary trees are considered leaf-similar if their leaf value sequence is 
# the same. 
# 
#  Return true if and only if the two given trees with head nodes root1 and 
# root2 are leaf-similar. 
# 
#  
#  Example 1: 
# 
#  
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,
# null,null,null,null,null,9,8]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each tree will be in the range [1, 200]. 
#  Both of the given trees will have values in the range [0, 200]. 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 1681 👎 55


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getNextInorderLeaf(stack):
            while stack:
                node = stack.pop()
                if node == -1:
                    node = stack.pop()
                    if node.right:
                        stack.append(node.right)
                elif not node.left and not node.right:
                    return node
                else:
                    stack.append(node)
                    stack.append(-1)
                    if node.left:
                        stack.append(node.left)
            return None

        stack1 = [root1]
        stack2 = [root2]
        while True:
            leaf1 = getNextInorderLeaf(stack1)
            leaf2 = getNextInorderLeaf(stack2)
            if not leaf1 and not leaf2:
                return True

            if (leaf1 and not leaf2) or (leaf2 and not leaf1):
                return False

            if leaf1.val != leaf2.val:
                return False
# leetcode submit region end(Prohibit modification and deletion)
