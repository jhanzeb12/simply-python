def log(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('../logs/log.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned {value}")

        return value
    return wrapper

@log
def hello_world(person):
    print(f"Hello {person}")

hello_world("Mike")