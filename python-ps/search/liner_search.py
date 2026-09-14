def find_max(arr):
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] >= maximum: 
            maximum = arr[i]
    return maximum

def find_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

def count_even(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count +=1
    return count

def search(arr, target): # O(n)
    for i in range(len(arr)):
        if arr[i]  == target:
            return i 
    return -1

arr = [1,24,6,2,6,8,4]
print(search(arr, 8))
print(f"max num in {arr} is {find_max(arr)}")
print(f"Sum of {arr} is {find_sum(arr)}")
print(f"count of even nums is {arr} is {count_even(arr)}")

