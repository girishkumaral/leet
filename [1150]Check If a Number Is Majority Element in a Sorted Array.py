# Given an integer array nums sorted in non-decreasing order and an integer 
# target, return true if target is a majority element, or false otherwise. 
# 
#  A majority element in an array nums is an element that appears more than 
# nums.length / 2 times in the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i], target <= 10⁹ 
#  nums is sorted in non-decreasing order. 
#  
#  Related Topics Array Binary Search 👍 302 👎 31


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def findsmaller(l, r):
            found = False

            while l <= r:
                if l == r:
                    return l-1, found
                m = (r-l) // 2 + l
                if not found and nums[m] == target:
                    found = True
                if not m:
                    return -1, found
                if nums[m-1] < target and nums[m] == target:
                    return m-1, found
                elif nums[m] >= target:
                    r = m-1
                else:
                    l = m+1
            return -1, found

        left, found = findsmaller(0, len(nums)-1)
        if not found:
            return False

        def findGreater(l, r):
            _found = False

            while l <= r:
                if l == r:
                    return r+1, _found
                m = (r-l) // 2 + l
                if not _found and nums[m] == target:
                    _found = True
                if m >= len(nums)-1:
                    return len(nums), _found
                if nums[m+1] > target and nums[m] == target:
                    return m + 1, _found
                elif nums[m] <= target:
                    l = m+1
                else:
                    r = m-1
            return len(nums), _found

        right, _ = findGreater(0, len(nums) - 1)
        print(left, right)

        if right-left-1 > len(nums) // 2:
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
