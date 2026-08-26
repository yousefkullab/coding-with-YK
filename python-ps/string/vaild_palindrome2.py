def valid_palindrome(text):
    left = 0
    rigth = len(text) - 1

    while left < rigth:
        if text[left] != text[rigth]:
            return (
                text[left:rigth] == text[left:rigth][::-1] 
                or 
                text[left+1:rigth+1] == text[left+1:rigth+1][::-1]
            )

        left += 1
        rigth -= 1    

    return True


print(valid_palindrome("abca")) 
print(valid_palindrome("abc")) 
print(valid_palindrome("abba")) 
