def object_decorator(class_):
   class_.__get_attr__orig = class_.__getattribute__
   def new_getattr(self, name):
      if name == "mileage":
          print("This is a decorator function. And the class attribute is accessed now.")
      return class_.__get_attr__orig(self, name)
   class_.__getattribute__ = new_getattr
   return class_

@object_decorator
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

car = Car("Toyota", "Camry", 2021, 15000)

print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")
print(f"Mileage: {car.mileage} kilometers")