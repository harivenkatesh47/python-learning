"""
Task 1: Access Control Whitelist Auditor
"""

def main():
    print("=== System Access Control Auditor ===")
    
    # 1 & 2. List to set deduplication
    raw_log = ["USR-1", "USR-2", "USR-3", "USR-1", "USR-4", "USR-2"]
    authorized_users = set(raw_log)
    print(f"Raw Log Entries       : {len(raw_log)}")
    print(f"Deduplicated Whitelist: {authorized_users} (Unique: {len(authorized_users)})")
    
    # 3 & 4. Modifying the set
    authorized_users.add("USR-5")
    print(f"Added User USR-5      : {authorized_users}")
    
    authorized_users.remove("USR-3")
    print(f"Revoked User USR-3    : {authorized_users}")
    
    # 5 & 6. Deletion safety checks
    print("\n--- Defensive Deletion Checks ---")
    authorized_users.discard("USR-99")
    print("Discarding 'USR-99'   : Operation executed cleanly without exception.")
    
    try:
        authorized_users.remove("USR-99")
    except KeyError as e:
        print(f"Removing 'USR-99'     : KeyError caught: {e} not found in whitelist.")
        
    # 7. Membership check
    is_authorized = "USR-2" in authorized_users
    print(f"User USR-2 Authorized : {is_authorized}")

if __name__ == "__main__":
    main()