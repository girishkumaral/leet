# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric 
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 👍 3690 👎 5217


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            #if i == j:
            #    return False
            if (ord('a') <= ord(s[i]) <= ord('z') or
                ord('A') <= ord(s[i]) <= ord('Z') or
                ord('0') <= ord(s[i]) <= ord('9')) and\
                    (ord('a') <= ord(s[j]) <= ord('z') or
                     ord('A') <= ord(s[j]) <= ord('Z') or
                    ord('0') <= ord(s[j]) <= ord('9')):
                if s[i].upper() != s[j].upper():
                    return False
                i += 1
                j -= 1
            else:
                if not (ord('a') <= ord(s[i]) <= ord('z') or\
                        ord('A') <= ord(s[i]) <= ord('Z') or
                        ord('0') <= ord(s[i]) <= ord('9')):
                    i += 1
                if not (ord('a') <= ord(s[j]) <= ord('z') or\
                        ord('A') <= ord(s[j]) <= ord('Z') or
                        ord('0') <= ord(s[j]) <= ord('9')):
                    j -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
