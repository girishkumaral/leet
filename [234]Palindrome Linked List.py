# Given the head of a singly linked list, return true if it is a palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,2,1]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 10⁵]. 
#  0 <= Node.val <= 9 
#  
# 
#  
# Follow up: Could you do it in O(n) time and O(1) space? Related Topics Linked 
# List Two Pointers Stack Recursion 👍 8907 👎 546


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)
