"""
Problem Description


Construct a class Circle that represents a Circle.


The class should support the following functionalities:-
perimeter() -> returns the perimeter of the circle
area() -> returns the area of the circle


Assume Π (pi) = 3.14 for calculations.
You may define any properties in the class as you see appropriate.


"""

class Circle:
    # Define properties here
    radius = 0
    pi = 3.14
    # Define constructor here
    def __init__(self,r) -> None:
        self.radius = r

    def perimeter(self):
        # Complete the function
        return 2 * self.pi * self.radius

    def area(self):
        # Complete the function
        return self.pi * self.radius * self.radius

a = Circle(3)  # Radius = 3
print(a.perimeter()) # 18.84
print(a.area()) # 28.26