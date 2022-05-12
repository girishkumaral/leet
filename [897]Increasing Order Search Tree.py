# Given the root of a binary search tree, rearrange the tree in in-order so 
# that the leftmost node in the tree is now the root of the tree, and every node has 
# no left child and only one right child. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree will be in the range [1, 100]. 
#  0 <= Node.val <= 1000 
#  
#  Related Topics Stack Tree Depth-First Search Binary Search Tree Binary Tree ?
# ? 3209 👎 629


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        First = None
        Tail = None
        while stack:
            node = stack.pop()
            if node == -1:
                node = stack.pop()
                stack.append(node.right)
                node.right = None
                if not First:
                    First = Tail = node
                else:
                    Tail.right = node
                    Tail = node
            elif node != None:
                stack.append(node)
                stack.append(-1)
                stack.append(node.left)
                node.left = None
        return First
# leetcode submit region end(Prohibit modification and deletion)
