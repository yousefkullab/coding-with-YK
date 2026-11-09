# Understand 
# INPUT array of nums and intger k
# OUTPUT return True if abs(i-j) <= k else False

# Example
# nums = [1,2,3,1], k = 3
# return True

# Brute Force, Time O(N^2), Space O(1) 
# class Solution:
#     def containsNearbyDuplicate(self, nums, k) -> bool:
#         for i in range(len(nums)):
#             for j in range(1+i, len(nums)):
#                 if (nums[i] == nums[j]) and abs(i-j) <= k:
#                     return True
#         else:
#             return False

# s = Solution()
# print(s.containsNearbyDuplicate([1,2,3,1], 3)) # True
# print(s.containsNearbyDuplicate([1,0,1,1], 1)) # True
# print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False


# Bottleneck (Problem) >>> we loop on all elements
# Optimize > use Hash Table ( Map )
# code
class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen:
                if i-last_seen[num] <= k:
                    return True
            last_seen[num] = i
        return False

# Test Case & Complixity Time O(n), Space O(n)
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3)) # True
print(s.containsNearbyDuplicate([1,0,1,1], 1)) # True
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False


