# Task 2: Smart Currency & Bill Splitter

try:
    # 1. Prompts
    total_bill = float(input("Enter total bill amount: $"))
    num_people = int(input("Enter number of people sharing the bill: "))

    # 2. Validate participant count to prevent division by zero
    if num_people <= 0:
        print("Validation Error: Number of participants must be greater than 0.")
    else:
        # 3. Compute exact share rounded to 2 decimal places
        exact_share = round(total_bill / num_people, 2)

        # 4. Split share into whole dollars and remaining cents using // and %
        # Convert total share to whole cents first for clean integer math
        total_cents = int(round(exact_share * 100))
        dollars = total_cents // 100
        cents = total_cents % 100

        # 5. Formatted output via f-strings
        print("\n--- Bill Breakdown ---")
        print(f"Total Bill: ${total_bill:.2f}")
        print(f"Participants: {num_people}")
        print(f"Share Per Person: ${exact_share:.2f}")
        print(f"Split Breakdown: {dollars} dollars and {cents} cents")

except ValueError:
    print("Error: Invalid numeric format entered.")