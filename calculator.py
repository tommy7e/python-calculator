class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if (b >= 0):
            for i in range(b):
                result = self.add(result, a)
        else:
            for i in range(b-b-b):
                result = self.subtract(result, a)
        return result

    def divide(self, a, b):
        if (b != 0):
            result = 0
            if (a > 0 and b > 0):
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
            elif (a > 0 and b < 0):
                b = b-b-b
                while a >= b:
                    a = self.subtract(a, b)
                    result -= 1
            elif (a < 0 and b > 0):
                a = a-a-a
                while a >= b:
                    a = self.subtract(a, b)
                    result -= 1
            else:
                a = a-a-a
                b = b-b-b
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1       
            return result
        else:
            return "fam. you just divided somethin with 0 and that ain't allowed by isaac newton or somethin."
    
    def modulo(self, a, b):
        if (a > 0 and b > 0):
            if (a<b):
                return a
            else:
                while a >= b:
                    self.subtract(a,b)
                return a
        elif (a < 0 and b < 0):
            if (a>b):
                return a
            else:
                while a <= b:
                    self.subtract(a,b)
                return a
        else:
            if (a<b):
                a = a-a-a
                while b <= a:
                    b += b
                return b-a
            else:
                b = b-b-b
                while a >= b:
                    b += b
                return a-b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))