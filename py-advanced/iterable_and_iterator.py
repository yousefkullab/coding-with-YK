
iterable = [1,2,3]  # iterable can be list tuple, set, dict, str 
iterator = iter(iterable) # iter() , next()

# __iter__()	Returns an Iterator
# __next__()	Returns the next item, or raises StopIteration when finished.

# print(iterable)
# print(iterator)
# print(next(iterator))

# build a custom Iterator
class CountToThree:
    def __init__(self):
        self.currrnet = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.currrnet > 3:
            raise StopIteration
        value = self.currrnet
        self.currrnet += 1
        return value

oneToThree = CountToThree()
iter(oneToThree)
print(next(oneToThree))
print(next(oneToThree))
print(next(oneToThree)) # StopIteration



    