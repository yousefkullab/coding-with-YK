# Arithmetic Operators
import math

if __name__ == '__main__':
    a = int(input("a= "))
    b = int(input("b= "))
    if a in range(int(math.pow(10, 10))) and b in range(int(math.pow(10, 10))):
        print(a + b)
        print(a - b)
        print(a * b)
    else:
        print("a, b not in range 0 to 10000000000")
        
# Software Engineer Joseph   
        