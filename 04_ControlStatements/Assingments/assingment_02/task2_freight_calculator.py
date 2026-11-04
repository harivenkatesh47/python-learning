def main():
    print("=== Freight & Tariff Logistics Engine ===")
    try:
        weight = float(input("Enter consignment weight (kg): "))
        
        if weight <= 0.0:
            print("\nError: Package weight must be strictly greater than 0.0 kg.")
        else:
            tier = input("Enter delivery speed (standard/express): ").strip().lower()
            is_fragile_input = input("Is cargo fragile? (yes/no): ").strip().lower()
            
            is_fragile = (is_fragile_input == "yes")
            
            # Nested branching for base shipping rate
            if weight <= 5.0:
                if tier == "express":
                    rate_per_kg = 80.0
                else:
                    rate_per_kg = 40.0
            elif weight <= 20.0:
                if tier == "express":
                    rate_per_kg = 120.0
                else:
                    rate_per_kg = 70.0
            else:
                if tier == "express":
                    rate_per_kg = 180.0
                else:
                    rate_per_kg = 110.0
                    
            base_charge = weight * rate_per_kg
            
            # Ternary operations for surcharges
            fragile_fee = 250.0 if is_fragile else 0.0
            surcharge = 150.0 if tier == "express" else 0.0
            
            total_invoice = base_charge + fragile_fee + surcharge
            
            # Itemized output
            print("\n--- Itemized Consignment Invoice ---")
            print(f"Gross Weight        : {weight:.2f} kg")
            print(f"Applied Rate Tier   : ₹{rate_per_kg:.2f} / kg")
            print(f"Base Freight Cost   : ₹{base_charge:.2f}")
            print(f"Fragile Surcharge   : ₹{fragile_fee:.2f}")
            print(f"Express Priority Fee: ₹{surcharge:.2f}")
            print("------------------------------------")
            print(f"Total Invoice Amount: ₹{total_invoice:.2f}")

    except ValueError:
        print("\nError: Invalid numeric input detected for weight.")

if __name__ == "__main__":
    main()