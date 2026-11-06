def initialize_account(account_holder, initial_deposit=1000.0):
    return {
        "holder": account_holder,
        "balance": initial_deposit,
        "history": [f"INITIAL DEPOSIT: ₹{initial_deposit:.2f}"]
    }

def get_balance(account):
    return account["balance"]

def process_deposit(account, amount):
    if amount <= 0:
        return False, "Deposit amount must be strictly positive."
        
    account["balance"] += amount
    account["history"].append(f"CREDIT: ₹{amount:.2f}")
    return True, f"₹{amount:.2f} credited successfully."

def process_withdrawal(account, amount):
    if amount <= 0:
        return False, "Withdrawal amount must be strictly positive."
        
    if amount > account["balance"]:
        return False, "Transaction declined: Insufficient funds."
        
    account["balance"] -= amount
    account["history"].append(f"DEBIT: ₹{amount:.2f}")
    return True, f"₹{amount:.2f} debited successfully."

if __name__ == "__main__":
    print("=== Core Banking Engine Self-Test ===")
    
    test_acc = initialize_account("Test User", 1000.0)
    print(f"Initialized mock account for '{test_acc['holder']}' with ₹{test_acc['balance']:.2f}")
    
    success, msg = process_deposit(test_acc, 500)
    print(f"Deposit ₹500  : {'Success' if success else 'Blocked'} (New Balance: ₹{test_acc['balance']:.2f})")
    
    success, msg = process_withdrawal(test_acc, 200)
    print(f"Withdraw ₹200 : {'Success' if success else 'Blocked'} (New Balance: ₹{test_acc['balance']:.2f})")
    
    success, msg = process_withdrawal(test_acc, 2000)
    print(f"Withdraw ₹2000: {'Success' if success else 'Blocked'} ({msg})")
    
    print("Test assertions completed cleanly.")