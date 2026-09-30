# Understand 
# input > list of nums and target 
# output > return two sum of index that sum of value = target

# Example 
# input > num = [2, 5, 12, 1, 7, 9], target = 13
# output > [2, 3]

# Brute Force Time O(n^2), Space O(1)
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
        
# num = [2, 5, 12, 1, 7, 9]
# target = 13
# print(twoSum(num, target))

# Problem > we search for all elements

# Optimize > use hash table

# code 
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    
# Test & Complexity Time O(n), Space O(n)
num = [2, 5, 12, 1, 7, 9]
target = 13
print(twoSum(num, target))


