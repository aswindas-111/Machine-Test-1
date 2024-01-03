class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = Calculator()

result_addition = obj.addition(a, b)
result_subtraction = obj.subtraction(a, b)

print("Addition result:", result_addition)
print("Subtraction result:", result_subtraction)
