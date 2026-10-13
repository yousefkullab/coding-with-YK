# Understand 
# INPUT array of nums 
# OUTPUT return True i any number apper tiwce in the array and False if the nums is distict

# Example
# nums = [1,2,3,1]
# return True 

# Brute Force, Time O(N^2), Space O(1) 
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         else:
#             return False

# s = Solution()
# print(s.containsDuplicate([1,2,3,1])) # True
# print(s.containsDuplicate([1,2,4,5])) # False

# Bottleneck (Problem) >>> We use Tow for loop ( compare all elements )
# Optimize > use hash table (set) 

# code 
class Solution:
    def containsDuplicate(self, nums) -> bool:
       return len(nums) != len(set(nums))

# Test Case & Complixity Time O(n), Space O(n)
s = Solution()
print(s.containsDuplicate([1,2,3,1])) # True
print(s.containsDuplicate([1,2,4,5])) # False
