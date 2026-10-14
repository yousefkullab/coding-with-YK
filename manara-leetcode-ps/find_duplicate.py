# Understand 
# INPUT array of nums 
# OUTPUT return the repeated number 

# Example 
# Input: nums = [1,3,4,2,2]
# Output: 2

# Brute Force, Time O(n^2), Space O(n)
# class Solution:
#     def findDuplicate(self, nums):
#         for i in range(len(nums)):
#                 for j in range(i+1, len(nums)):
#                      if nums[i] == nums[j]:
#                         return nums[j]
# s = Solution()
# print(s.findDuplicate([1,3,4,2,2]))

# Bottleneck > we check twice in array and this is cost time

# Optimize > use hash table (set)

# code 
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# Test & Complixit Time O(n), Space O(n)
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
