"""
Problem Description

Construct a class Rectangle that represents a rectangle.
The class should support the following functionalities:-
perimeter() -> returns the perimeter of the rectangle
area() -> returns the area of the rectangle
You may define any properties in the class as you see appropriate.

"""

class Rectangle:
    # Define properties here
    length = 0
    breadth = 0
    
    # Define constructor here
    def __init__(self,l,b) -> None:
        self.length = l
        self.breadth = b

    def perimeter(self):
        # Complete the function
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
        # Complete the function
    
        
a = Rectangle(2, 3)  # Length = 2, Breadth = 3
print(a.perimeter()) # Should give 10
print(a.area()) # Should give 6