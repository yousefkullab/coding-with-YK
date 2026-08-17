# Write a function
import math
def is_leap(year):
    leap = False
    
    if year >= 1900 and year <= math.pow(10, 5):
        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            return True
        else:
            return False
    else: 
        print("Out of range!")
    
    return leap

year = int(input())
print(is_leap(year))


