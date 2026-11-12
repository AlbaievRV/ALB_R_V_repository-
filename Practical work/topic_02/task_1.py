import math


def calculate_discriminant(a, b, c):
  """Calculates the discriminant of a quadratic equation: D = b^2 - 4ac."""
  return (b**2) - (4 * a * c)


def solve_quadratic():
  """Finds the roots of a quadratic equation based on user input."""
  print("Quadratic equation: a*x^2 + b*x + c = 0")

  try:
    a = float(input("Enter coefficient a (a != 0): "))

    if a == 0:
      print("Error: 'a' cannot be 0 in a quadratic equation!")
      return

    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    d = calculate_discriminant(a, b, c)
    print(f"\nFor equation {a}x^2 + {b}x + {c} = 0:")
    print(f"Discriminant (D) = {d}")

    if d > 0:
      x1 = (-b + math.sqrt(d)) / (2 * a)
      x2 = (-b - math.sqrt(d)) / (2 * a)
      print("The equation has two real roots:")
      print(f"x1 = {x1}")
      print(f"x2 = {x2}")
    elif d == 0:
      x = -b / (2 * a)
      print("The equation has one real root:")
      print(f"x = {x}")
    else:
      print("The equation has no real roots (only complex ones).")

  except ValueError:
    print("Error: Please enter valid numbers only!")


# Run the function
solve_quadratic()
