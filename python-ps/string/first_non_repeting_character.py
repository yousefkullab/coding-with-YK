def first_non_repeting_character(text): 
    for i in text:
        if text.count(i) == 1:
            return i
    return f"All characters are repeted '{text}'"

# Big O Time 
# loop O(n)
# count() O(n)
# Total O(n^2)
# Space O(1)

print(first_non_repeting_character("sthdt"))
print(first_non_repeting_character("swiss"))
print(first_non_repeting_character("aabbcc"))