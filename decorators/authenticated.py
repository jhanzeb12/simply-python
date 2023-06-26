user = None
def is_authenticated(func):
    def wrapper():
        if user is not None:
            Exception("User is not authenticated.")
        else:
            func()
    return wrapper


@is_authenticated
def hello_world():
    print('Hello World!!');


hello_world()