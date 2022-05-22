# Given a positive integer num, write a function which returns True if num is a 
# perfect square else False. 
# 
#  Follow up: Do not use any built-in library function such as sqrt. 
# 
#  
#  Example 1: 
#  Input: num = 16
# Output: true
#  Example 2: 
#  Input: num = 14
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2^31 - 1 
#  
#  Related Topics Math Binary Search 👍 2303 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        if num == 1:
            return True
        while l < r:
            #print(l, r)
            m = (r-l)//2 + l
            if m * m == num:
                return True
            elif m * m > num:
                if (m-1) * (m-1) < num:
                    return False
                r = m - 1
            else:
                if (m+1) * (m+1) > num:
                    return False
                l = m + 1
        return (l * l == num)
# leetcode submit region end(Prohibit modification and deletion)
