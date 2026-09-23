# Understand 
#   * Input nums, k 
#   * Output Kth largest element 

# Midd Example 
#   nums = [3,2,1,5,6,4], k = 2
#   return 5


# Brute Force Time O(nlogn), Space O(n)*
# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]
# s = Solution()
# print(s.findKthLargest([3,2,1,5,6,4], 2))

# Problem > we use liner sort it is cost O(nlogn)

# Optimize > use priority queue ( heap )

# Code 

import heapq 
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap_nums = []
        for num in nums:
            heapq.heappush(heap_nums, num)
            if len(heap_nums) > k:
                heapq.heappop(heap_nums)
        return heap_nums[0]

# Test & Complexity Time O(log k), Spave O(log k)

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

