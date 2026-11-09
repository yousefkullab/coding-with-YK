# Understand
#   * Input points[i] = [Xi, Yi] and k num of points
#   * return the k points closest to the origin (0,0)
#   * use the distance law about two points and law for the origin (0,0)

# Middle Example 
# points = [[-1, 3], [-2, 2]] , k = 1
# output = [[-2, 2]]

# Brute Force Time O(n logn), Space O(n)
# class Solution:
#     def kClosest(self, points, k):
#         res = []
#         # calcalute distance for every points
#         for point in (points):
#             point_distance =  (point[0]**2) + (point[1]**2)
#             res.append([point_distance, point])
#         res.sort()
#         Kpoints = []
#         for i in res:
#             Kpoints.append(i[1])
#         return Kpoints[:k]

# s = Solution()
# print(s.kClosest([[-1, 3], [-2, 2]], 1))

# Bottleneck > res.sort() when sort all points but we need only k closest points

# Optimize > use Max heap

# code 
import heapq
class Solution:
    def kClosest(self, points, k):
        heap = []
        for point in points:
            distance = ((point[0]**2) + (point[1]**2))
            heapq.heappush(heap, [-distance, point])

            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]

# Test & Complixity Time O(n log k), Space O(k)

s = Solution()
print(s.kClosest([[-1, 3], [-2, 2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
