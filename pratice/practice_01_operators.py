# Practice: Calculate the total bill including a 15% tip
# Instructions:
# 1. Ask the user for the meal cost (float).
# 2. Calculate a 15% tip.
# 3. Print the original cost, tip amount, and total bill.

meal_cost = float(input("Enter meal cost: $"))
tip = meal_cost * 0.15
total = meal_cost + tip

print(f"\nMeal: ${meal_cost}")
print(f"Tip (15%): ${tip}")
print(f"Total: ${total}")