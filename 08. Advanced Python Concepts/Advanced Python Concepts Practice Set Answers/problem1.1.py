def logger(func):
    def wrapper():
        print("Function is being called!")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello")

say_hello()