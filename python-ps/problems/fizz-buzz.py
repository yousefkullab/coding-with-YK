nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for num in nums:
    if num % 15 == 0:
        print(f'{num}fizz-buzz', end=' ')
    elif num % 3 == 0:
        print(f'{num}fizz', end=' ')
    elif num % 5 == 0:
        print(f'{num}buzz', end=' ')
    else:
        print(f'{num}', end=' ')

