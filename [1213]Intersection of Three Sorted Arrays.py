# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing 
# order, return a sorted array of only the integers that appeared in all three 
# arrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
#  
# 
#  Example 2: 
# 
#  
# Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = 
# [521,682,1337,1395,1764]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr1.length, arr2.length, arr3.length <= 1000 
#  1 <= arr1[i], arr2[i], arr3[i] <= 2000 
#  
#  Related Topics Array Hash Table Binary Search Counting 👍 442 👎 22


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        final = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                final.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                m = min(arr1[i], arr2[j], arr3[k])
                if m == arr1[i]:
                    i += 1
                if m == arr2[j]:
                    j += 1
                if m == arr3[k]:
                    k += 1
        return final

# leetcode submit region end(Prohibit modification and deletion)
