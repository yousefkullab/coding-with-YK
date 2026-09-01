class Solution():

    # def isPowerOfTwo(self, n:int) -> bool:
    #         if n <= 0:
    #             return False
    #         return (n & (n-1)) == 0
    # Time  → O(1) 
    # Space → O(1) 
    
    def isPowerOfTwo(self, n:int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True

s = Solution()
print(s.isPowerOfTwo(1))  # True
print(s.isPowerOfTwo(16)) # True
print(s.isPowerOfTwo(3))  # False

# Time Complexity = O(log n)
# Space Complexity = O(1)
