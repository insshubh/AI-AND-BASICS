def greet(fx):
    def wrapper(*args, **kwargs):
        print("Hello Guyz")
        result = fx(*args, **kwargs)
        print(result)
        print("Bye Guys")
    return wrapper

@greet
def test(a, b):
    return a+b

test(5, 3)
