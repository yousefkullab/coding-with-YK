nums = [1,2,3,4,5,6]

print(nums)

# accessing elements in a list
print(nums[3]) # average/worse case O(1)

# search element in a list
def search_element(nums, traget): # average/worse case O(n)
    for num in nums:
        if num == traget:
            return True
    return False

print(search_element(nums, 3))

# Inserting an element in a list
def add_element(nums, element): # average/worse case O(1) amortized
    nums.append(element) 
    return nums

print(add_element(nums, 5))

# deleting an element in a list
def delete_element(nums, element): # average/worse case O(n)
    if element in nums:
        nums.remove(element)
    return nums

print(delete_element(nums, 3))

# traversing a list
def traverse_list(nums): # average/worse case O(n)
    for num in nums:
        print(num, end=" ")

traverse_list(nums)


