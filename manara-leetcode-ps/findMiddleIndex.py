# Understand 
#   Input > nums 
#   Output > index for sum(left side ) == sum(right side)
#   Constirans >>>> num[i] + nums[i+1] ..... nums[middle]  ... nums[middle+1] .... nums[len(nums)-1]
#   if middleIndex == 0 then left sum = 0
#   if middleIndex == len(nums)-1 then right sum = 0

# Middle Example 
# Input: nums = [2,3,-1,8,4]
# Output: 3 

# Brute Force O(n^2)
# def find_middle_index(nums):
#     for i in range(len(nums)):
#         left_sum = sum(nums[:i])
#         right_sum = sum(nums[i+1:])
#         if left_sum == right_sum: 
#             return i
#     return -1
# print(find_middle_index([2,3,-1,8,4]))

# Problem > we make sum every once in the iteration

# Optimze > Use Prefix Sum

# code 
def find_middle_index(nums):
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1

# Test & Complexity Time O(n), Space O(1)
print(find_middle_index([2,3,-1,8,4]))
print(find_middle_index([1,-1,4]))
print(find_middle_index([2,5]))


