# Run the code in any code editors like VS code to get the required results... Thank you ;>
# The operations available in this calculator are : +, -, *, /, sin, cos, tan, sec, csc, cot, sqrt, pow, and log 
import math

class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operator = None

    def set_values(self, operator, num1, num2=0):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        if self.operator == '+':
            result = self.num1 + self.num2
            print(f"The result of addition of {self.num1} and {self.num2} is: ", result)
        elif self.operator == '-':
            result = self.num1 - self.num2
            print(f"The result of subtraction of {self.num1} and {self.num2} is: ", result)
        elif self.operator == '*':
            result = self.num1 * self.num2
            print(f"The result of multiplication of {self.num1} and {self.num2} is: ", result)
        elif self.operator == '/':
            result = self.num1 / self.num2
            print(f"The result of division of {self.num1} and {self.num2} is: ", result)
        elif self.operator == 'sin':
            result = math.sin(self.num1)
            print(f"The result of sine of {self.num1} is:", result)
        elif self.operator == 'cos':
            result = math.cos(self.num1)
            print(f"The result of cos of {self.num1} is:", result)
        elif self.operator == 'tan':
            result = math.tan(self.num1)
            print(f"The result of tan of {self.num1} is:", result)
        elif self.operator == 'sec':
            if self.num1 == 0:
                print("Invalid input for secant: denominator cannot be 0")
                return
            result = 1 / math.cos(self.num1)
            print(f"The result of sec of {self.num1} is:", result)
        elif self.operator == 'csc':
            if self.num1 == 0:
                print("Invalid input for cosecant: denominator cannot be 0")
                return
            result = 1 / math.sin(self.num1)
            print(f"The result of csc of {self.num1} is:", result)
        elif self.operator == 'cot':
            if math.tan(self.num1) == 0:
                print("Invalid input for cotangent: denominator cannot be 0")
                return
            result = 1 / math.tan(self.num1)
            print(f"The result of cot of {self.num1} is:", result)

        elif self.operator == 'sqrt':
            if self.num1 < 0:
                print("Invalid input for square root: number cannot be negative")
                return
            result = math.sqrt(self.num1)
            print(f"The resulting square root of {self.num1} is: ", result)

        elif self.operator == 'pow':
            result = math.pow(self.num1, self.num2)
            print(f"The value of {self.num1} ^ {self.num2} is:", result)

        elif self.operator == 'log':
            if self.num1 <= 0:
                print("Invalid input for logarithm: number must be greater than 0")
                return
            result = math.log(self.num1, self.num2)
            print("The result of logarithm is:", result)

        else:
            print("Invalid operator. Please enter +, -, *, /, sin, cos, tan, sec, csc, cot, sqrt, pow, or log")
            

calculator = Calculator()

while True:
    operation = input("Enter an operation: +, -, *, /, sin, cos, tan, sec, csc, cot, sqrt, pow, log, quit: ")
    if operation == "quit":
        break
    try:
        f = float(input("Enter the 1st value: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if operation in ['+', '-', '*', '/', 'pow', 'log']:
        try:
            s = float(input("Enter the 2nd value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        calculator.set_values(operation, f, s)
    else:
        calculator.set_values(operation, f)
    calculator.calculate()  # Call the calculate method to perform the calculation
    
