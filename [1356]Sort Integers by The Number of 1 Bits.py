# You are given an integer array arr. Sort the integers in the array in 
# ascending order by the number of 1's in their binary representation and in case of two 
# or more integers have the same number of 1's you have to sort them in ascending 
# order. 
# 
#  Return the array after sorting it. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should 
# just sort them in ascending order.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 500 
#  0 <= arr[i] <= 10⁴ 
#  
#  Related Topics Array Bit Manipulation Sorting Counting 👍 1027 👎 45


# leetcode submit region begin(Prohibit modification and deletion)
NibbleToBitCount = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 1,
    9: 2,
    10: 2,
    11: 3,
    12: 2,
    13: 3,
    14: 3,
    15: 4
}


def byte2bitCount(num):
    return NibbleToBitCount[(0xf & num)] + NibbleToBitCount[(0xf0 & num) >> 4]


def int2bitCount(num):
    return ByteToBitCount[(0xff & num)] + \
           ByteToBitCount[(0xff00 & num) >> 8] + \
           ByteToBitCount[(0xff0000 & num) >> 16] + \
           ByteToBitCount[(0xff000000 & num) >> 24]


ByteToBitCount = dict()
for i in range(256):
    ByteToBitCount[i] = byte2bitCount(i)


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitstoInt = defaultdict(lambda: list())
        for num in arr:
            bitstoInt[int2bitCount(num)].append(num)
        keys = sorted(bitstoInt.keys())
        final = []
        for key in keys:
            bitstoInt[key].sort()
            final.extend(bitstoInt[key])
        return final
# leetcode submit region end(Prohibit modification and deletion)
