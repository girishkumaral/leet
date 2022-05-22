# Given a string s, return true if a permutation of the string could form a 
# palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "code"
# Output: false
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aab"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "carerac"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5000 
#  s consists of only lowercase English letters. 
#  
#  Related Topics Hash Table String Bit Manipulation 👍 878 👎 63


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        C = Counter(s)
        OddCount = 0
        for key in C.keys():
            if C[key] % 2 is not 0:
                OddCount += 1
            if OddCount > 1:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
