# Give a binary string s, return the number of non-empty substrings that have 
# the same number of 0's and 1's, and all the 0's and all the 1's in these 
# substrings are grouped consecutively. 
# 
#  Substrings that occur multiple times are counted the number of times they 
# occur. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's 
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of 
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are 
# not grouped together.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal 
# number of consecutive 1's and 0's.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either '0' or '1'. 
#  
#  Related Topics Two Pointers String 👍 2899 👎 619


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        run = 1
        suf = 0
        current = s[0]
        other = {
            "0": "1",
            "1": "0"
        }
        i = 1
        final = []
        switch = False
        while i < len(s):
            #print(current, suf, run, switch, final, "---")
            if s[i] == current:
                if switch:
                    switch = False
                    if suf == 1:
                        run = 1
                        #current = other[current]
                        suf = 0
                        final.append(1 * other[current]+ current * 1)
                    else:
                        run = suf
                        suf = 1
                        current = other[current]
                        final.append(current * 1+1 * other[current])
                else:
                    run += 1
            else:
                switch = True
                suf += 1
                if suf < run:
                    final.append(current*suf+suf*other[current])
                else:
                    final.append(current * suf + suf * other[current])
                    run = suf
                    current = other[current]
                    suf = 0
                    switch = False
            i += 1
        #print(final)
        return len(final)

# leetcode submit region end(Prohibit modification and deletion)
