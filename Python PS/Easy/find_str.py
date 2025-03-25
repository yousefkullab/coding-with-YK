# Find a string

# NOTE: String letters are case-sensitive.

# constrains
# 1 <= len(string) <= 200

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        pro_sub = string[i:len(sub_string)+i]
        if sub_string == pro_sub:
            count+=1
    return count

if __name__ == '__main__':
    string_input = input("Enter the string: ")
    substring_input = input("Enter the substring: ")
    count = count_substring(string_input, substring_input)
    
    print(f"count: {count}")
    
    
    
# Software Engineer Joseph.