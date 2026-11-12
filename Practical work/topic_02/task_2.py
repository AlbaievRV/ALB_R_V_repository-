def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    return "Error: Division by zero!"
  return x / y


print("--- Calculator (if-else) ---")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
  result = add(num1, num2)
  print(f"Result: {num1} + {num2} = {result}")
elif operator == "-":
  result = subtract(num1, num2)
  print(f"Result: {num1} - {num2} = {result}")
elif operator == "*":
  result = multiply(num1, num2)
  print(f"Result: {num1} * {num2} = {result}")
elif operator == "/":
  result = divide(num1, num2)
  print(f"Result: {num1} / {num2} = {result}")
else:
  print("Error: Invalid operator!")