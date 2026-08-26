class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in word_dict:
                if s[i] in word_dict.values():
                    return False
                word_dict[pattern[i]] = s[i]
            else:
                if word_dict[pattern[i]] != s[i]:
                    return False
        return True
            



solution = Solution()
s = "dog cat cat dog"
pattern = "abac"
result = solution.wordPattern(pattern, s)
print(result)  # Output: True