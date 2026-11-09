# Undersrand 
#   * inptu num1,num2 where num1 is subset of num2
#   * output num same lentgh of num1 
#   * if element of num1 has next grether elements add it if not replace it with -1

# Middle Example 
#   num1 [4,1,2], num2 [1,3,4,2]
#   return [-1, 3, -1]

# Brute Force, Time O(n*m), Space(n)
# def nextGreaterElement(nums1, nums2):
#     res = []
#     for i in nums1:
#         index = nums2.index(i) 
#     # search elements after i 
#         for j in range(index +1, len(nums2)):
#             if i < nums2[j]:
#                 res.append(nums2[j])
#                 break
#         else:
#             res.append(-1)
#     return res

# print(nextGreaterElement([4,1,2], [1,3,4,2]))

# Problem > we have O(n) nums2.index(i)

# Optimize > Use Monotonic Stack 

# code
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack= []
        next_greather = {}

        for num in nums2:
            while stack and stack[-1] < num:
                previous  = stack.pop()
                next_greather[previous] = num

            stack.append(num)

        for i in stack:
            next_greather[i] = -1

        res = []

        for x in nums1:
            res.append(next_greather[x])
        return res

# Test & Complexity Time O(n+m), Space O(m)

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))

    

