import banking_core as bank

def main():
    print("=== Enterprise Banking CLI ===")
    name = input("Enter Account Holder Name: ").strip()
    
    try:
        init_amount = float(input("Enter Initial Deposit (or press Enter for default ₹1000): ") or "1000")
        account = bank.initialize_account(name, init_amount)
    except ValueError:
        print("Invalid input. Initializing with default ₹1000.00.")
        account = bank.initialize_account(name)
        
    print(f"\nWelcome, {account['holder']}! Account initialized.")

    while True:
        print("\n--- Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. View Transaction History")
        print("5. Exit Session")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            print(f"Current Balance: ₹{bank.get_balance(account):.2f}")
            
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: ₹"))
                success, message = bank.process_deposit(account, amount)
                print(f"[{'SUCCESS' if success else 'FAILED'}]: {message}")
            except ValueError:
                print("[ERROR]: Invalid amount format.")
                
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                success, message = bank.process_withdrawal(account, amount)
                print(f"[{'SUCCESS' if success else 'FAILED'}]: {message}")
            except ValueError:
                print("[ERROR]: Invalid amount format.")
                
        elif choice == "4":
            print("\n--- Transaction Ledger ---")
            for record in account["history"]:
                print(f"  * {record}")
                
        elif choice == "5":
            print(f"Thank you for banking with us, {account['holder']}. Session closed.")
            break
            
        else:
            print("Invalid selection. Please choose an option between 1 and 5.")

if __name__ == "__main__":
    main()