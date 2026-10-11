# Understand 
# Input > list[str] 
# Output > list[list[str]]groups of strs that is anagram

# Middle Example 
# strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]

# Brute Force Time O(n^2), Space O(n*m)
# class Solution:
#     def groupAnagrams(self, strs):
#         groups = []
#         keys = []
#         for word in strs:
#             key = "".join(sorted(word))
#             found = False
#             for i in range(len(groups)):
#                 if keys[i] == key:
#                     groups[i].append(word)
#                     found = True
#                     break
#             if not found:
#                 groups.append([word])
#                 keys.append(key)
#         return groups

# s = Solution()
# print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Problem > we search in a lot of previous groups 

# Optimize > use hash table dict

# code 
class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

# Test & Complixty, Time O(n*m logm), Space(n*m)
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([]))
print(s.groupAnagrams(["", ""]))
