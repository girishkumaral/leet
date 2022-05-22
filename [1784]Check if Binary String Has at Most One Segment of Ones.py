# Given a binary string s without leading zeros, return true if s contains at 
# most one contiguous segment of ones. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "110"
# Output: true 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s[i] is either '0' or '1'. 
#  s[0] is '1'. 
#  
#  Related Topics String 👍 171 👎 543


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        segment = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if s[i] == '1':
                segment += 1
            i = j
        return segment == 1
# leetcode submit region end(Prohibit modification and deletion)
