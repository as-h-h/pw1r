import numpy as np 
from collections import Counter

#################################################################################
class Rectangle:
    def __init__(self, width=1.0, height=1.0):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor=1.0):
        if factor < 0:
            raise ValueError("Scale factor must be positive.")
        return Rectangle(self.width * factor, self.height * factor)
    
#################################################################################

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = list(coefficients)
 
    def padding(self, other):
        diff = len(self.coefficients) - len(other.coefficients)
        if diff > 0:
            other.coefficients += [0] * diff
        elif diff < 0:
            self.coefficients += [0] * abs(diff)
        self.coefficients = np.array(self.coefficients)
        other.coefficients = np.array(other.coefficients)
 
    def drop(self):
        coeffs = list(self.coefficients)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.coefficients = coeffs
        return self
 
    def deg(self):
        self.drop()
        return len(self.coefficients) - 1
 
    def __str__(self):
        terms = []
        for i, c in enumerate(self.coefficients):
            if c == 0:
                continue
            if i == 0:
                terms.append(str(c))
            elif i == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{i}")
        return " + ".join(terms) if terms else "0"
 
    def __neg__(self):
        new_coeffs = [-coef for coef in self.coefficients]
        return Polynomial(new_coeffs)
 
    def __add__(self, other_poly):
        a = Polynomial(self.coefficients)
        b = Polynomial(other_poly.coefficients)
        a.padding(b)
        nums = a.coefficients + b.coefficients
        return Polynomial(nums).drop()
 
    def __sub__(self, other_poly):
        a = Polynomial(self.coefficients)
        b = Polynomial(other_poly.coefficients)
        a.padding(b)
        nums = a.coefficients - b.coefficients
        return Polynomial(nums).drop()
 
    def __mul__(self, other_poly):
        n = len(self.coefficients)
        m = len(other_poly.coefficients)
        result = [0] * (n + m - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other_poly.coefficients):
                result[i + j] += a * b
        return Polynomial(result).drop()
 
    def __eq__(self, other_poly):
        a = Polynomial(self.coefficients).drop()
        b = Polynomial(other_poly.coefficients).drop()
        return a.coefficients == b.coefficients
 
    def __call__(self, x):
        X = [x**i for i in range(len(self.coefficients))]
        val = np.dot(self.coefficients, X)
        return val

#################################################################################

class Urn:
    def __init__(self, balls=None):
        if balls is None:
            self.counts = Counter()
        else:
            self.counts = Counter(balls)
 
    def add(self, color, count=1):
        self.counts[color] += count
 
    def count(self, color):
        return self.counts[color]
 
    def total(self):
        return sum(self.counts.values())
 
    def probability(self, color):
        t = self.total()
        if t == 0:
            return 0.0
        return self.count(color) / t
 
    def __str__(self):
        return f"Urn({self.counts})"