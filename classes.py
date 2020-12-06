
#############################       KLASY      #############################################


def complex_numbers():
    class Complex:
        def __init__(self, re, im):
            self.re = re
            self.im = im

        def __str__(self):
            return '(%s, %si)' % (self.re, self.im)

        def __add__(self, other):
            re1 = self.re
            im1 = self.im
            re2 = other.re
            im2 = other.im
            result_re = re1 + re2
            result_im = im1 + im2
            return Complex(result_re, result_im)

        def __sub__(self, other):
            re1 = self.re
            im1 = self.im
            re2 = other.re
            im2 = other.im
            result_re = re1 - re2
            result_im = im1 - im2
            return Complex(result_re, result_im)

        def __mul__(self, other):
            re1 = self.re
            im1 = self.im
            re2 = other.re
            im2 = other.im
            result_re = (re1 * re2) - (im1 * im2)
            result_im = (re1 * im2) + (im1 * re2)
            return Complex(result_re, result_im)

    class Calculator:

        def __init__(self, num1 = None, num2 = None, operation = None):
            self.num1 = num1
            self.num2 = num2
            self.operation = operation

        def __call__(self):
            if self.operation == '+':
                return self.num1 + self.num2
            elif self.operation == "-":
                return self.num1 - self.num2
            elif self.operation == '*':
                return self.num1 * self.num2
            else:
                print("Podales zla operacje")

        def calculate(self, operation):
            operation_parsed = operation.split(' ')
            z1 = self.complex_parser(operation_parsed[0])
            z2 = self.complex_parser(operation_parsed[2])
            sign = operation_parsed[1]
            return Calculator(z1, z2, sign)

        @staticmethod
        def complex_parser(complex_with_bracket):
            pure_complex = complex_with_bracket[1:-1]
            if '+' in pure_complex:
                coefs_complex = pure_complex.split('+')
                comp_number = Complex(float(coefs_complex[0]), float(coefs_complex[1][:-1]))
            else:
                real_minus = False
                if pure_complex[0] == '-':
                    real_minus = True
                    pure_complex = pure_complex[1:]
                coefs_complex = pure_complex.split('-')
                real_num = float(coefs_complex[0]) if not real_minus else -float(coefs_complex[0])
                comp_number = Complex(real_num, -float(coefs_complex[1][:-1]))
            return comp_number
    operation = input()
    calc = Calculator().calculate(operation)
    result = calc()
    print(result)


if __name__ == '__main__':
    print("Podaj działanie w formacie (liczba1)  (działanie) (liczba2)")
    complex_numbers()