def find_max(numbers): # Time O(n) , Space O(1)
    max_num = numbers[0]
    for number in numbers:
        if max_num < number:
            max_num = number
    return max_num

def count_even(numbers): # Time O(n), Space O(1)
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count +=1
    return count

def has_duplicates(numbers): # Time O(n^2), Space O(1)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    else: return False


if __name__ == "__main__":

    numbers =  [10, 5, 8, 20, 3, 7]
    print(f"The max number in {numbers} is {find_max(numbers)}")
    print(f"The count of even nums in {numbers} is {count_even(numbers)}")
    print(f"{numbers} Has duplicates {has_duplicates(numbers)}")

