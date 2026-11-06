# 1. Define a function that returns multiple values (automatically packed as a tuple)
def split_currency(total_amount):
    """
    Splits a raw currency float into whole major units (rupees) and fractional minor units (paise).
    
    Parameters:
        total_amount (float): The total payment amount.
        
    Returns:
        tuple: A packed tuple containing (rupees (int), paise (int)).
    """
    rupees = int(total_amount)
    paise = round((total_amount - rupees) * 100)
    return rupees, paise


# 2. Define a function that computes tax and returns multiple values
def compute_tax_breakdown(base_amount, tax_rate_percent):
    """
    Calculates tax liability and gross payable amount.
    
    Parameters:
        base_amount (float): The base taxable amount.
        tax_rate_percent (float): The applicable tax rate percentage.
        
    Returns:
        tuple: A packed tuple containing (base_amount, tax_amount, grand_total).
    """
    tax_amount = round(base_amount * (tax_rate_percent / 100), 2)
    grand_total = round(base_amount + tax_amount, 2)
    return base_amount, tax_amount, grand_total


# 3. Execution body
def main():
    print("=== Financial Denomination & Tax Splitter ===")
    
    print("\n--- Currency Decomposition ---")
    raw_amount = 12450.75
    # Capture the packed tuple
    raw_tuple = split_currency(raw_amount)
    print(f"Packed Tuple Received : {raw_tuple}")
    print(f"Tuple Verification    : {isinstance(raw_tuple, tuple)}")
    
    # Unpack the tuple into discrete variables
    rupees, paise = split_currency(raw_amount)
    print(f"Unpacked Rupees       : ₹{rupees}")
    print(f"Unpacked Paise        : {paise} paise")
    
    print("\n--- Tax Assessment Split ---")
    # Unpack all three returned values simultaneously
    base_val, tax_val, total_val = compute_tax_breakdown(5000.0, 18.0)
    print(f"Taxable Base Amount   : ₹{base_val:.2f}")
    print(f"Tax Levied (18.0%)    : ₹{tax_val:.2f}")
    print(f"Grand Payable Total   : ₹{total_val:.2f}")


if __name__ == "__main__":
    main()