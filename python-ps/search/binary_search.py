from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # found target
            if nums[mid] == target:
                return mid

            # left side sorted
            if nums[left] <= nums[mid]:

                # target inside left side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side sorted
            else:

                # target inside right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
    print(s.search([1], 0))  # Output: -1
