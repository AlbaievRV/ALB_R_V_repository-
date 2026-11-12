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


print("--- Calculator (match-case) ---")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
  case "+":
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
  case "-":
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
  case "*":
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
  case "/":
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
  case _:
    print("Error: Invalid operator!")