"""
Construct a class called ComplexNumber which stores two properties

real - The real part
imaginary - The imaginary part

The name of the properties should be strictly real and imaginary


Implement the following functionalities inside this class :-

add(ComplexNumber) -> Returns an object of ComplexNumber having sum of the two complex numbers.

subtract(ComplexNumber) -> Returns an object of ComplexNumber having difference of the two complex numbers.

multiply(ComplexNumber) -> Returns an object of ComplexNumber having multiplication of the two complex numbers.

divide(ComplexNumber) -> Returns an object of ComplexNumber having division of the two complex numbers.
"""

class ComplexNumber:

    real = 0
    imaginary = 0

    # Define constructor here
    def __init__(self,real = 0,imaginary = 0) -> None:
        self.real = real
        self.imaginary = imaginary


    def add(self, x: "ComplexNumber")->"ComplexNumber":
        a = self.real + x.real
        b = self.imaginary + x.imaginary
        return ComplexNumber(a,b)
        # Complete the function

    def subtract(self, x: "ComplexNumber")->"ComplexNumber":
        a = self.real - x.real
        b = self.imaginary - x.imaginary
        return ComplexNumber(a,b)
        # Complete the function

    def multiply(self, x: "ComplexNumber")->"ComplexNumber":
        a = (self.real * x.real) - (self.imaginary * x.imaginary)
        b = (self.real * x.imaginary) + (self.imaginary * x.real)
        return ComplexNumber(a,b)
        # Complete the function

    def divide(self, x: "ComplexNumber")->"ComplexNumber":
        a = ((self.real * x.real)+(self.imaginary * x.imaginary))/((x.real * x.real)+(x.imaginary * x.imaginary))
        b = ((self.imaginary * x.real)-(self.real * x.imaginary))/((x.real * x.real)+(x.imaginary * x.imaginary))
        return ComplexNumber(a,b)
        # Complete the function
    def __str__(self):
        return f"{self.real}"+( "-" if self.imaginary < 0 else "+" ) + f"{self.imaginary}i"
a = ComplexNumber(10, 5)
b = ComplexNumber(2, 3)
c1 = a.add(b) 
c2 = a.subtract(b)
c3 = a.multiply(b)
c4 = a.divide(b)

print(c1,c2,c3,c4)