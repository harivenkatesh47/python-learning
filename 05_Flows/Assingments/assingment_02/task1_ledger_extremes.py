def main():
    print("=== Retail Day-End Ledger Audit Engine ===")
    
    # 1. Initialize receipts
    daily_receipts = [1250.50, 450.00, 3200.75, 89.00, 2150.00, 740.25, 4100.00, 310.50]
    print(f"Receipts Monitored     : {len(daily_receipts)} transactions")
    
    # 2. Initialize tracking variables
    total_revenue = 0.0
    highest_sale = daily_receipts[0]
    lowest_sale = daily_receipts[0]
    
    # 3. Manual iteration and accumulation
    for receipt in daily_receipts:
        total_revenue += receipt
        if receipt > highest_sale:
            highest_sale = receipt
        if receipt < lowest_sale:
            lowest_sale = receipt
            
    # 4. Averages and filtering
    average_sale = round(total_revenue / len(daily_receipts), 2)
    
    high_tier_sales = []
    standard_sales = []
    
    for receipt in daily_receipts:
        if receipt >= 2000.0:
            high_tier_sales.append(receipt)
        else:
            standard_sales.append(receipt)
            
    # 5. Formatted Output
    print("\n--- Derived Financial Metrics (Manual Loop Reductions) ---")
    print(f"Gross Daily Revenue    : ₹{total_revenue:.2f}")
    print(f"Peak Transaction Value : ₹{highest_sale:.2f}")
    print(f"Lowest Ticket Value    : ₹{lowest_sale:.2f}")
    print(f"Average Ticket Value   : ₹{average_sale:.2f}")
    
    print("\n--- Transaction Tier Breakdown ---")
    print(f"High-Tier Sales (>= ₹2000) : {high_tier_sales}")
    print(f"Standard Sales (< ₹2000)  : {standard_sales}")

if __name__ == "__main__":
    main()