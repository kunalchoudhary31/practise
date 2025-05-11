import datetime
import functools

def timestamp(func):
    """A decorator that prints a timestamp before executing the decorated function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp_str}] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@timestamp
def add(x, y):
    """Adds two numbers."""
    return x + y

@timestamp
def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

@timestamp
def greet(name):
    """Greets a person."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    sum_result = add(5, 3)
    print(f"Result of addition: {sum_result}\n")

    product_result = multiply(4, 6)
    print(f"Result of multiplication: {product_result}\n")

    greeting = greet("Alice")
    print(f"Greeting: {greeting}\n")