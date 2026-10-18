# Decorator > used to add additional behavioer to the func with out edit the original code
# In Backend used : Logging,Timing, Auth, Cashing

import time 
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"Function {func.__name__}")
        print(f"Execution Time: {elapsed_time:.4f} seconds")

        return res 
    return wrapper

@timer
def calculate_total(a, b):
    time.sleep(2)
    return a + b

# res = calculate_total(10,20)


# Decorators with Arguments
def retry(max_attempts):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attemp in range(max_attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as error:
                    last_error = error
            raise last_error
        return wrapper
    return decorator

attempts = 0

@retry(max_attempts=3)
def fetch_data():
    global attempts
    attempts += 1

    if attempts < 3:
        raise ConnectionError("Temporary failure")

    return "Data received"


print(fetch_data())
print("Attempts:", attempts)
