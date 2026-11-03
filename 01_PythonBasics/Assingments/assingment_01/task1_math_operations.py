# Task 1: Perform Basic Mathematical Operations


def main():
  print("=== Basic Mathematical Operations ===")

  try:
    # 1. Take two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # 2. Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division by zero
    division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

    # 3. Display results
    print("\nResults:")
    print(f"Addition:       {num1} + {num2} = {addition}")
    print(f"Subtraction:    {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division:       {num1} / {num2} = {division}")

  except ValueError:
    print("Invalid input! Please enter valid numeric values.")


if __name__ == "__main__":
  main()