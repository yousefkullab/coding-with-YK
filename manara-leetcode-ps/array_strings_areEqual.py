from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
     # return ''.join(word1) == ''.join(word2)
        s1, s2 = "", ""
        for c in word1:
            s1 += c
        for c in word2:
            s2 += c

        return s1 == s2

s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(s.arrayStringsAreEqual(["abc", "d", "fg"], ["abcddefg"]))

