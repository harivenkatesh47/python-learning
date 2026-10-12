# Task 3: Bill Splitting & Currency Breakdown

try:
    # 1. Prompts
    total_bill = float(input("Enter the total bill amount: $"))
    people_count = int(input("Enter the total number of people sharing: "))

    # 2. Comparison operator validation to prevent division by zero
    if people_count > 0:
        # 3. Compute individual's share rounded to 2 decimal places
        individual_share = round(total_bill / people_count, 2)

        # 4. Floor division (//) and modulus (%) to extract dollars and cents
        individual_cents_total = int(round(individual_share * 100))
        whole_dollars = individual_cents_total // 100
        remaining_cents = individual_cents_total % 100

        # 6. Formatted split summary
        print(f"\nTotal Amount: ${total_bill:.2f}")
        print(f"Split Between: {people_count} people")
        print(f"Each Person Pays: ${individual_share:.2f}")
        print(f"Currency Units: {whole_dollars} dollars and {remaining_cents} cents")
    else:
        print("Error: The number of people must be strictly greater than 0.")

# 5. Exception handling for non-numeric input
except ValueError:
    print("Error: Please provide valid numeric values for the bill and participant count.")