# Understand 
# input arrat of nums 
# output k most frequent elements 
# Constraints k range [1, the len(set(nums))] 

# Middle Example 
# nums = [1,1,1,2,2,3], k = 2
# return nums = [1,2]


# Brute Force Time O(nlogn), Space O(n)
# class Solution: 
#     def topKFrequent(self, nums, k):
#         table = {}
#         for i in nums:
#             if i not in table.keys():
#                 table[i] = 1
#             else:
#                 table[i] += 1
#         sorted_val = sorted(table.items(), key=lambda item:item[1], reverse=True)
#         return [item[0] for item in sorted_val[:k]]


# Bottleneck > we need sort all elements but we need only top k sorted()

# Optimize > used heapq ( min heap )

# code
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap[:k]]


# Test & Complixity Time O(n log k), Space O(n+k)
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))


