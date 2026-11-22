class Solution:
    def fractionAddition(self, expression: str) -> str:
        class Fraction:
            def __init__(self, sign: str | int, numerator: str | int, denominator: str | int) -> None:
                self.numerator = int(numerator)
                self.denominator = int(denominator)
                self.sign = -1 if sign in ("-", -1) else 1

            def gcd(self, a: int, b: int) -> int:
                while b:
                    a, b = b, a % b
                return a

            def lcm(self, other: "Fraction") -> int:
                return (self.denominator * other.denominator) // self.gcd(self.denominator, other.denominator)

            def normalizeDenominator(self, other: "Fraction") -> None:
                new_denominator = self.lcm(other)
                self.numerator *= new_denominator // self.denominator
                other.numerator *= new_denominator // other.denominator
                self.denominator = new_denominator
                other.denominator = new_denominator

            def add(self, other: "Fraction") -> "Fraction":
                self.normalizeDenominator(other)
                new_numerator = self.numerator * self.sign + other.numerator * other.sign
                new_sign = -1 if new_numerator < 0 else 1
                return Fraction(new_sign, abs(new_numerator), self.denominator)

            def toIrreducibleFraction(self) -> "Fraction":
                if self.numerator == 0:
                    self.denominator = 1
                    self.sign = 1
                    return self

                r = self.gcd(self.numerator, self.denominator)
                self.numerator //= r
                self.denominator //= r
                return self

            def toString(self) -> str:
                prefix = "-" if self.sign == -1 and self.numerator != 0 else ""
                return f"{prefix}{self.numerator}/{self.denominator}"

        list_of_fractions: list[Fraction] = []
        temp = ""
        sign = "+"
        numerator = ""

        # Parse the expression character by character
        for s in expression:
            if s in ("+", "-"):
                if temp:
                    list_of_fractions.append(Fraction(sign, numerator, temp))
                    temp = ""
                sign = s
            elif s == "/":
                numerator = temp
                temp = ""
            else:
                temp += s

        # Append the final fraction after the loop finishes
        if temp:
            list_of_fractions.append(Fraction(sign, numerator, temp))

        res = list_of_fractions[0]
        for f in list_of_fractions[1:]:
            res = res.add(f)

        return res.toIrreducibleFraction().toString()