# Task 2: Create a Personalized Greeting


def main():
  print("=== Personalized Greeting Program ===")

  # 1. Take first name and last name as input
  first_name = input("Enter your first name: ").strip()
  last_name = input("Enter your last name: ").strip()

  # 2. Concatenate into a full name
  full_name = f"{first_name} {last_name}"

  # 3. Print personalized greeting
  print(f"\nHello, {full_name}! Welcome to the Python Program.")


if __name__ == "__main__":
  main()