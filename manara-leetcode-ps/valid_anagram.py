# Understand 
# input two string s, t
# output check if two strings is anagram of not

# Middle Example 
# input: s = "anagram", t = "nagaram"
# output ture

# Brute Force Time O(n^2) , Space O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         else:
#             for i in s:
#                 for j in t:
#                     if i in t and j in s:
#                         return True
#                     else:
#                         return False

# Problem > When Find a common char while return True and this is not right 

# Optimize > use hash > frequency 

# code 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 0 
            chars[s[i]] += 1


        for i in range(len(s)):
            if t[i] not in chars:
                chars[t[i]] = 0 
            chars[t[i]] -= 1

        for key, val in chars.items():
            if val != 0:
                return False
            
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
# print(s.isAnagram("car", "rat"))
