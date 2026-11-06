def standard_fee(amount):
    return 15.0 + (amount * 0.015)

def international_fee(amount):
    return 100.0 + (amount * 0.038)

def premium_client_fee(amount):
    return amount * 0.005

def process_payment(transaction_id, amount, fee_strategy_func):
    applied_fee = fee_strategy_func(amount)
    total_charged = round(amount + applied_fee, 2)
    
    record = {
        "txn_id": transaction_id,
        "amount": amount,
        "fee": round(applied_fee, 2),
        "total": total_charged
    }
    return record

def main():
    strategies = {
        "domestic": standard_fee,
        "overseas": international_fee,
        "vip": premium_client_fee,
    }

    print("=== Higher-Order Payment Gateway Engine ===")
    
    print("\n--- Processing Transaction TXN-8801 (Domestic) ---")
    dom_txn = process_payment("TXN-8801", 4500.00, strategies["domestic"])
    print(f"Raw Amount      : ₹{dom_txn['amount']:.2f}")
    print(f"Calculated Fee  : ₹{dom_txn['fee']:.2f}")
    print(f"Total Deducted  : ₹{dom_txn['total']:.2f}")
    
    print("\n--- Processing Transaction TXN-8802 (Overseas) ---")
    int_txn = process_payment("TXN-8802", 18200.00, strategies["overseas"])
    print(f"Raw Amount      : ₹{int_txn['amount']:.2f}")
    print(f"Calculated Fee  : ₹{int_txn['fee']:.2f}")
    print(f"Total Deducted  : ₹{int_txn['total']:.2f}")
    
    print("\n--- Processing Transaction TXN-8803 (VIP Tier) ---")
    vip_txn = process_payment("TXN-8803", 50000.00, strategies["vip"])
    print(f"Raw Amount      : ₹{vip_txn['amount']:.2f}")
    print(f"Calculated Fee  : ₹{vip_txn['fee']:.2f}")
    print(f"Total Deducted  : ₹{vip_txn['total']:.2f}")

if __name__ == "__main__":
    main()