# Calculate the avg of list of numbers
def calculate_avg(*numbers):
    if not numbers:
        return 0
    sum = 0 
    for num in numbers:
        sum += num
    avg = sum / len(numbers)
    return avg

# print(calculate_avg(1,2,3,4,5))

# Find the max number in a list of numbers 
def find_max(*numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(1,2,3,4,5))


# Check if a num is even 
def is_even(num):
    return num % 2 == 0

# print(is_even(4))  


# Count the number of vowels in a string
def count_vowels(str):
    count = 0 
    for char in str:
        if char.lower() in 'aeiou':
            count +=1
    return count

print(count_vowels
      ("Yousef khaled kullab"))


# Calculate the total of a list of numbers 
def calculate_total(*numbers):
    total = 0 
    for num in numbers:
        total += num
    return total

print(calculate_total(1,2,3,4,5))


# Check if a number is positive
def is_positive(num):
    if num > 0:
        return True
    else:
        return False
