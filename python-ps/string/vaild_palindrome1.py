def valid_palindrome(s: str) -> bool:
    return s == s[::-1]

# Why I used this approach: simple and efficient 
# Time complexity: O(n) where n is the length of the string
# Space complexity: O(n) due to the space used for the reversed string