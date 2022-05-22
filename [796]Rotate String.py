# Given two strings s and goal, return true if and only if s can become goal 
# after some number of shifts on s. 
# 
#  A shift on s consists of moving the leftmost character of s to the rightmost 
# position. 
# 
#  
#  For example, if s = "abcde", then it will be "bcdea" after one shift. 
#  
# 
#  
#  Example 1: 
#  Input: s = "abcde", goal = "cdeab"
# Output: true
#  Example 2: 
#  Input: s = "abcde", goal = "abced"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, goal.length <= 100 
#  s and goal consist of lowercase English letters. 
#  
#  Related Topics String String Matching 👍 1849 👎 86


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        i = 0
        if len(s) != len(goal):
            return False
        while i < l:
            #print(s)
            if s[0] == goal[0]:
                if s == goal:
                    return True
            s = s[1::] + s[0]
            i += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
