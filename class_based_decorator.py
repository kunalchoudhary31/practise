import datetime

class WarehouseDecorator:
    
    def __init__(self, material):
        self.material = material
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            t = start.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{t}] Calling function: {func.__name__}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    
@WarehouseDecorator("wood")  # Replace "wood" with the material of your choice)
def add(a, b):
    """Adds two numbers."""
    return a + b

@WarehouseDecorator("metal")  # Replace "metal" with the material of your choice)
def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def greet(name):
    """Greets a person."""
    return f"Hello, {name}!"

print(add(5, 3))
print(multiply(4, 6))
