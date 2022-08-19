"""
Problem Description
Construct a class Fraction which stores a fraction. It should contain the

-Numerator
-Denominator

Assume denominator will never be 0.

The class should support the following functionalities

add(Fraction) -> Returns the sum of two fractions

subtract(Fraction) -> Returns the difference of two fractions

multiply(Fraction) -> Returns the product of two fractions

The fraction returned needs to be in the simplest form. If the fraction is p/q then p and q must be co-prime.

You may define any properties in the class as you see appropriate.


"""

class Fraction:

    # Define constructor here
    numerator = 0
    denominator = 0

    def __init__(self,n,d) -> None:
        self.numerator = n
        self.denominator = d

    def makeSame(self,x):
        return Fraction(self.numerator * x, self.denominator * x)

    def add(self, a):
        # Complete the function
        t1 = self.makeSame(1)
        t2 = a.makeSame(1)
        if a.denominator != self.denominator:
            t1 = self.makeSame(a.denominator)
            t2 = a.makeSame(self.denominator)
        num = t1.numerator + t2.numerator
        deno = t1.denominator
        return (Fraction(num,deno)).simplify()

    def subtract(self, a):
        # Complete the function
        t1 = self.makeSame(1)
        t2 = a.makeSame(1)
        if a.denominator != self.denominator:
            t1 = self.makeSame(a.denominator)
            t2 = a.makeSame(self.denominator)
        num = t1.numerator - t2.numerator
        deno = t1.denominator
        return (Fraction(num,deno)).simplify()

    def simplify(self):
        gcd = self.findGCD(self.numerator,self.denominator)
        gcd = (gcd * -1) if gcd < 0 else gcd
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
        return self

    def findGCD(self,a,b):
        if a < b:
            a,b = b,a
        r = a % b
        while r != 0:
            a,b = b,r
            r = a % b
        return b

    def multiply(self, a):
        return Fraction(self.numerator * a.numerator,self.denominator * a.denominator).simplify()

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    # 2 4
    # 3 5

x = Fraction(2, 3)  # 2/3
y = Fraction(4, 5) # 4/5
z = x.add(y) # 22/15
print(z)
z = x.subtract(y) # -2/15
print(z)
z = x.multiply(y) # 8/15
print(z)
