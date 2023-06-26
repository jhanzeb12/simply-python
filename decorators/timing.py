import time

def timed(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        fname = function.__name__
        print(f"{fname} took {end-start} seconds to execute!")
        return value
    return wrapper

@timed
def ranged(x):
    result = 0
    for i in range(1, x):
        result += i

    return result

print(ranged(100000))