# Given a string num which represents an integer, return true if num is a 
# strobogrammatic number. 
# 
#  A strobogrammatic number is a number that looks the same when rotated 180 
# degrees (looked at upside down). 
# 
#  
#  Example 1: 
# 
#  
# Input: num = "69"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: num = "88"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: num = "962"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num.length <= 50 
#  num consists of only digits. 
#  num does not contain any leading zeros except for zero itself. 
#  
#  Related Topics Hash Table Two Pointers String 👍 456 👎 775


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reflection = {
            '1': '1',
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': '9',
            '7': None,
            '8': '8',
            '9': '6',
            '0': '0'
        }
        if len(num) == 0:
            return True
        if len(num) == 1:
            if num[0] == '0' or num[0] == '8' or num[0] == '1':
                return True
            return False

        left = 0
        right = len(num)-1
        while left <= right:
            if left == right:
                if reflection[num[left]] == num[left]:
                    return True
                return False
            if not reflection[num[left]] or not reflection[num[right]]:
                return False
            if reflection[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
