# You have some apples and a basket that can carry up to 5000 units of weight. 
# 
#  Given an integer array weight where weight[i] is the weight of the iᵗʰ apple,
#  return the maximum number of apples you can put in the basket. 
# 
#  
#  Example 1: 
# 
#  
# Input: weight = [100,200,150,1000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of 
# weights is 1450.
#  
# 
#  Example 2: 
# 
#  
# Input: weight = [900,950,800,1000,700,800]
# Output: 5
# Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 
# 5 of them.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= weight.length <= 10³ 
#  1 <= weight[i] <= 10³ 
#  
#  Related Topics Array Greedy Sorting 👍 152 👎 13


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        run = 0
        count = 0
        for w in weight:
            run += w
            if run <= 5000:
                count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
