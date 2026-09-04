# def validPalindrome(s:str) -> bool:
#     for c in s:
#         if not c.isalnum():
#             s = s.replace(c, "")
#     s = s.lower()
#     return s == s[::-1]

# def validPalindrome(s:str) -> bool:
#     cleand = ''
#     for c in s:
#         if  c.isalnum():
#             cleand += c.lower()
#     left = 0
#     right = len(cleand)-1

#     while left < right:
#         if cleand[left] != cleand[right]:
#             return False
#         left +=1
#         right-=1
#     return True

def validPalindrome(s:str) -> bool:
    left = 0
    right = len(s)-1
    while left < right:
        if not s[left].isalnum():
            left +=1
            continue
        if not s[right].isalnum():
            right -=1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left +=1
        right -=1
    return True


if __name__ == '__main__':
    print(validPalindrome("A man, a plan, a canal: Panama"))
    print(validPalindrome("race a car"))

    
