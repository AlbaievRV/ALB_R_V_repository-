def calculate_discriminant(a, b, c):
  discriminant = (b**2) - (4 * a * c)
  return discriminant


print("Quadratic equation: a*x^2 + b*x + c = 0")

try:
  a = float(input("Enter coefficient a (a != 0): "))
  
  if a == 0:
    print("Error: 'a' cannot be 0 in a quadratic equation!")
  else:
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    # Calculating discriminant
    d = calculate_discriminant(a, b, c)
    print(f"\nFor equation {a}x^2 + {b}x + {c} = 0:")
    print(f"Discriminant (D) = {d}")

    if d > 0:
      print("The equation has two real roots.")
    elif d == 0:
      print("The equation has one real root.")
    else:
      print("The equation has no real roots (only complex ones).")

except ValueError:
  print("Error: Please enter valid numbers only!")