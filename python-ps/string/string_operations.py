def count_vowels(text): # Time O(n), Space O(1)
    count = 0 
    for char in text.lower():
        if char in ['a', 'i', 'e', 'o', 'u']:
            count += 1
    return count

def reverse_string(text): # Time O(n^2), Space O(n)
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

    # return text[::-1] # Time/Space O(n)


def is_palindrome(text): # Time/Space O(n)
    return text == reverse_string(text)

