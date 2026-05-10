class Calculator:
    @staticmethod
    def Sum( num1, num2):
       return num1 + num2
    @staticmethod
    def Diff( num1, num2):
        return num1 - num2  
    @staticmethod
    def Mult( num1, num2):
        return num1 * num2
    @staticmethod
    def Div( num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    @staticmethod
    def fact(num_fact):
        if num_fact < 0:
            return "Factorial is not defined for negative numbers"
        elif num_fact == 0 or num_fact == 1:
            return 1
        else:
            result = 1
            for i in range(2, num_fact + 1):
                result *= i
            return result
    @staticmethod
    def Pow(base_pow, exp_num):
        nump = 1
        for i in range(exp_num):
            nump = nump * base_pow
        return nump
# aa =  Calculator()
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num_fact = int(input("Enter a number to find its factorial: "))
base_pow, exp_num = map(int,input("Enter the (base, exponent) : ").split())
reslt_sum = Calculator.Sum(num1, num2)
reslt_diff = Calculator.Diff(num1, num2)
reslt_mult = Calculator.Mult(num1, num2)
reslt_div = Calculator.Div(num1, num2)
reslt_fact = Calculator.fact(num_fact)
reslt_pow = Calculator.Pow(base_pow, exp_num)
print("\n   **Results:**   ")
print (f"**the sum of {num1} and {num2} is: {reslt_sum}\n**the difference of {num1} and {num2} is: {reslt_diff}" )
print (f"**the multiplication of {num1} and {num2} is: {reslt_mult}\n**the division of {num1} and {num2} is: {reslt_div}" )
print (f"**the power of {base_pow} to the {exp_num} is: {reslt_pow}\n**the factorial of {num_fact} is: {reslt_fact}")
