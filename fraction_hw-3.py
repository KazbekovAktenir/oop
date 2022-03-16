def hcf(a, b):
    if a == 0:
        return b
    else:
        return hcf(b % a, a)


class Fraction:

    def __init__(self, numerator, denumerator):
        hcf1 = hcf(numerator, denumerator)
        self.numerator = numerator // hcf1
        self.denumerator = denumerator // hcf1

    def __str__(self):
        if self.denumerator == 1:
            return str(self.numerator)

        elif self.numerator > self.denumerator:
            return str(self.numerator // self.denumerator) + " " + \
                   str(Fraction(self.numerator % self.denumerator, self.denumerator))
        else:
            return str(self.numerator) + "/" + str(self.denumerator)

    def __add__(self, other):
        new_numerator = self.numerator * other.denumerator + other.numerator * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numerator, new_denumerator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denumerator - other.numerator * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numerator, new_denumerator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numerator, new_denumerator)

    def __floordiv__(self, other):
        new_numerator = self.numerator // other.numerator
        new_denumerator = self.denumerator // other.denumerator
        return Fraction(new_numerator, new_denumerator)


a = Fraction(3, 12)
b = Fraction(7, 49)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
