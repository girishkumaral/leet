# Given a characters array letters that is sorted in non-decreasing order and a 
# character target, return the smallest character in the array that is larger 
# than target. 
# 
#  Note that the letters wrap around. 
# 
#  
#  For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#  
# 
#  Example 2: 
# 
#  
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#  
# 
#  Example 3: 
# 
#  
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= letters.length <= 10⁴ 
#  letters[i] is a lowercase English letter. 
#  letters is sorted in non-decreasing order. 
#  letters contains at least two different characters. 
#  target is a lowercase English letter. 
#  
#  Related Topics Array Binary Search 👍 1662 👎 1519


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        minLarge = len(letters)-1
        while l <= r:
            m = (r-l)//2 + l
            if ord(letters[m]) > ord(target):
                minLarge = min(minLarge, m)
                r = m - 1
            else:
                l = m + 1
        if letters[minLarge] <= target and minLarge == len(letters)-1:
            return letters[0]
        return letters[minLarge]
# leetcode submit region end(Prohibit modification and deletion)
