# for use when you know number of dublicates
# while user when you don't know the number of dublicates

for i in range(10, 5, -1): # reverse order
    print(i, end=" ")

print()

# break , continue

count = 0
while count < 5:
    print(count, end=" ")
    count += 1
    if count == 3:
        break 

print()

for num in range(5):
    if num == 2:
        continue

    print(num, end=" ")

print()

# nested loops
for i in range(1):
    for j in range(10):
        print(f"{i} + {j} = {i+j}")

# loop in dict 

user = {
    "name": "Yousef",
    "age": 24
}

user = {
    "name": "Yousef",
    "age": 24
}

for key, value in user.items():
    print(key, value)

# enumerate used to track indexs
numbers = [4,2,5,6,8]
for i, num in enumerate(numbers):
    print(i, num)



    