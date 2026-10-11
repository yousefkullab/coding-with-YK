# Understand 
# Input array of int
# Output true if the num of occurrences of each value in the array is unique or false otherwise.

# Middle Example 
# arr = [1,2,2,1,1,3]
# retur True

# Brute Force Time O(n^2), Space O(n)
# class Solution:
#     def uniqueOccurrences(self, arr: list[int]) -> bool:
#         unique = set(arr)
#         counts = []
#         for num in unique:
#             counts.append(arr.count(num))
#         for i in range(len(counts)):
#             for j in range(i+1, len(counts)):
#                 if counts[i] == counts[j]:
#                     return False
#         return True
       
# s = Solution()
# print(s.uniqueOccurrences([1,2,2,1,1,3,2]))
            
# Problem > We use 2 for loop and it is cost time 

# Optimize > use hash table ( Counter )

# code 
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        uo = {}
        for num in arr:
            if num in uo:
                uo[num] += 1 
            else:
                uo[num] = 1
        return len(uo.values()) == len(set(uo.values()))
    
# Test & Complixity Time O(n), Space O(n)
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3,2]))
            

