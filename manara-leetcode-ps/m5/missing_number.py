# Understand 
# Input array of int numbers in range [0, n]
# Output int number that are missing for the range [0,n]

# Example:
# Input: [3,0,1]
# Output: 2 

# Brute force, Time complexity O(n^2), Space complexity O(1)
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         for i in range(len(nums) + 1):
#             if i not in nums:
#                 return i
# s = Solution()
# print(s.missingNumber([3,0,1]))

# Bottleneck > loop twice, to check if the number is in the array or not

# Optimize > used hast table (set)

# code 
class Solution:
    def missingNumber(self, nums):
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
        return -1

# Test Case & Complixity Time O(N), Space O(n)
s = Solution()
print(s.missingNumber([3,0,1]))

