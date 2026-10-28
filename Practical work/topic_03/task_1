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


print("--- Continuous Calculator ---")
print("Type 'exit' as operator to quit the program.\n")

while True:
  operator = input("Enter operator (+, -, *, /) or 'exit' to quit: ")

  if operator == "exit":
    print("Exiting calculator. Goodbye!")
    break

  if operator in ("+", "-", "*", "/"):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Error: Please enter valid numbers!\n")
      continue

    match operator:
      case "+":
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}\n")
      case "-":
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}\n")
      case "*":
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}\n")
      case "/":
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}\n")
  else:
    print("Error: Invalid operator! Try again.\n")