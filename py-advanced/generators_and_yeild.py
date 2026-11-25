def get_numbers():
    return [1, 2, 3]

print(get_numbers())

# Generator > used when we want to procude value on demands.
# return Ends the function, Returns a value once, Function execution ends
# yield  Pauses the function, Can produce multiple values, Execution can resume later

def count():
    yield 10
    yield 20
    yield 30

numbers = count()

print(next(numbers))
print(next(numbers))
print(list(numbers))

# Lazy Evaluation
def numbersOfM():
    for i in range(1_000_000):
        yield i

countToM = numbersOfM()

print(next(countToM))
print(next(countToM))
print(next(countToM))
