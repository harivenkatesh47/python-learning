def main():
    print("=== Transaction Risk Screener ===")
    try:
        amount = float(input("Enter Transaction Amount (₹): "))
        is_intl_input = input("Is this an international transaction? (yes/no): ").strip().lower()
        is_verified_input = input("Is the client device verified? (yes/no): ").strip().lower()

        # Boolean conversion
        is_international = (is_intl_input == "yes")
        device_verified = (is_verified_input == "yes")

        # Risk classification
        if amount <= 0:
            routing_action = "Invalid Transaction Amount"
        elif amount > 200000 and not device_verified:
            routing_action = "High Risk: Immediate Freeze"
        elif is_international and amount > 50000:
            routing_action = "Medium Risk: Manual Review Required"
        elif device_verified and amount <= 50000:
            routing_action = "Low Risk: Auto-Approved"
        else:
            routing_action = "Standard Processing: Routine Clearance"

        # Formatted breakdown
        print("\n--- Screening Verdict ---")
        print(f"Transaction Amount : ₹{amount:.2f}")
        print(f"International Flag : {is_international}")
        print(f"Device Verified    : {device_verified}")
        print(f"Routing Action     : {routing_action}")

    except ValueError:
        print("\nError: Invalid transaction amount. Please enter a valid number.")

if __name__ == "__main__":
    main()