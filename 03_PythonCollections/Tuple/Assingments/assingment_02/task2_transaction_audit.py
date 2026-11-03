"""
Task 2: Transaction Audit History
"""

def main():
    print("=== Financial Transaction Auditor ===")
    
    # 1, 2 & 3. Aggregations
    transactions = (1200.50, 450.00, -210.25, 3400.00, -150.00, 890.75)
    total_volume = sum(transactions)
    largest_deposit = max(transactions)
    largest_withdrawal = min(transactions)
    average_tx = round(total_volume / len(transactions), 2)
    
    print(f"Ledger Transactions : {transactions}")
    print(f"Total Volume Net    : {total_volume}")
    print(f"Largest Deposit     : {largest_deposit}")
    print(f"Largest Withdrawal  : {largest_withdrawal}")
    print(f"Average Transaction : {average_tx}")
    
    print("\n--- Immutability Verification ---")
    
    # 4 & 5. Immutability test and concatenation update
    try:
        transactions.append(500.00)
    except AttributeError as e:
        print(f"Append Trapped      : AttributeError caught: {e}")
        
    updated_ledger = transactions + (500.00,)
    print(f"Updated Ledger      : {updated_ledger}")

if __name__ == "__main__":
    main()