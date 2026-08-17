def count(n):
    # base case 
    if n == 0:
        return
    # recursive 
    print(n)
    return count(n-1)


print(count(5))