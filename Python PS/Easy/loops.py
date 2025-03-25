# Loops

import math

if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 20:
        for num in range(n):
            print(int(math.pow(num, 2)))