# A sentence is a string of single-space separated words where each word 
# consists only of lowercase letters. 
# 
#  A word is uncommon if it appears exactly once in one of the sentences, and 
# does not appear in the other sentence. 
# 
#  Given two sentences s1 and s2, return a list of all the uncommon words. You 
# may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
#  Example 2: 
#  Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s1.length, s2.length <= 200 
#  s1 and s2 consist of lowercase English letters and spaces. 
#  s1 and s2 do not have leading or trailing spaces. 
#  All the words in s1 and s2 are separated by a single space. 
#  
#  Related Topics Hash Table String 👍 923 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        print(words1, words2)
        C1 = Counter()
        C2 = Counter()
        for w in words1:
            C1[w] +=1

        for w in words2:
            C2[w] += 1

        final = []
        for key in C1.keys():
            if C1[key] == 1 and C2[key] == 0:
                final.append(key)
        for key in C2.keys():
            if C2[key] == 1 and C1[key] == 0:
                final.append(key)
        return final
# leetcode submit region end(Prohibit modification and deletion)
