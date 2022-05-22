# Given two non-negative integers, num1 and num2 represented as string, return 
# the sum of num1 and num2 as a string. 
# 
#  You must solve the problem without using any built-in library for handling 
# large integers (such as BigInteger). You must also not convert the inputs to 
# integers directly. 
# 
#  
#  Example 1: 
# 
#  
# Input: num1 = "11", num2 = "123"
# Output: "134"
#  
# 
#  Example 2: 
# 
#  
# Input: num1 = "456", num2 = "77"
# Output: "533"
#  
# 
#  Example 3: 
# 
#  
# Input: num1 = "0", num2 = "0"
# Output: "0"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 10⁴ 
#  num1 and num2 consist of only digits. 
#  num1 and num2 don't have any leading zeros except for the zero itself. 
#  
#  Related Topics Math String Simulation 👍 3265 👎 550


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        final = ""
        while i >= 0 or j >= 0:
            tmp1 = 0
            tmp2 = 0
            if i >= 0:
                tmp1 = int(num1[i])
                i -= 1
            if j >= 0:
                tmp2 = int(num2[j])
                j -= 1
            tmp = tmp1+tmp2+carry
            final = str(tmp%10) + final
            carry = tmp//10
        if carry:
            final = str(carry)+final
        return final
# leetcode submit region end(Prohibit modification and deletion)
