system_status = "IDLE"
transaction_count = 0

def demonstrate_shadowing():
    system_status = "BUSY_LOCAL"
    print(f"Inside function      : system_status = {system_status}")
    return None

def record_transaction(amount):
    global transaction_count, system_status
    
    transaction_count += 1
    system_status = "ACTIVE"
    
    print(f"Processed transaction of ₹{amount:.2f} -> Global Count: {transaction_count}")

def reset_audit_counter():
    global transaction_count, system_status
    
    transaction_count = 0
    system_status = "IDLE"

def main():
    print("=== Variable Scope & Shadowing Diagnostic ===")
    print(f"Initial Global State : Status = {system_status} | Count = {transaction_count}")
    
    print("\n--- 1. Testing Local Variable Shadowing ---")
    demonstrate_shadowing()
    print(f"Outside function     : system_status = {system_status} (Global unmutated)")
    
    print("\n--- 2. Modifying Global State via 'global' ---")
    record_transaction(2500.00)
    record_transaction(1200.00)
    print(f"Current Global State : Status = {system_status} | Count = {transaction_count}")
    
    print("\n--- 3. Resetting Global Scope ---")
    reset_audit_counter()
    print(f"Audit counter reset  : Status = {system_status} | Count = {transaction_count}")

if __name__ == "__main__":
    main()