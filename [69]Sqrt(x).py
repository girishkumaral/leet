# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and 
# only the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part 
# is truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
#  Related Topics Math Binary Search 👍 3847 👎 3208


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        l = 1
        r = x
        s = 0
        while l <= r:
            if r == l:
                return int(min(s, l))
            m = (r-l)/2 + l
            if m * m > x:
                if int(m)*int(m) <= x:
                    return int(m)
                r = m
                s = m
            elif m * m < x:
                l = m
            else:
                return int(m)

# leetcode submit region end(Prohibit modification and deletion)
