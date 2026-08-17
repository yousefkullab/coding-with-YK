def tow_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
        
   
num = [2, 5, 12, 1, 7, 9]
target = 13
print(tow_sum(num, target))

# Why i used this approach: simple and correct solution without requiring extra data structures, but there is a better approach used hashmap.
# Time complexity: O(n^2) due to nested loops
# Space complexity: O(1) no extra space used
