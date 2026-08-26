from typing import List
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixs = set()
        for a in arr1:
            while a > 0:
                if a in prefixs:
                    break
                prefixs.add(a)
                a = a // 10
        r = 0
        for b in arr2:
            while b > r:
                if b in prefixs:
                    r = b
                    break
                b = b // 10
        return len(str(r)) if r else 0
    
if __name__ == "__main__":
    arr1 = [1,10,100]
    arr2 = [1000]
    solution = Solution()
    result = solution.longestCommonPrefix(arr1, arr2)
    print(result)

        