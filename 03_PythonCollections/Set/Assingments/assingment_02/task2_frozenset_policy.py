"""
Task 2: Frozen Set Security Policy Engine
Module: Module 06 - Tuples, Sets & Dictionaries
"""

def main():
    print("=== Frozen Set Policy Manager ===")
    
    # 1. Immutable profiles
    read_only = frozenset(["read", "view_logs"])
    admin_perms = frozenset(["read", "write", "delete", "view_logs"])
    
    print(f"Audit Role Permissions  : {read_only}")
    print(f"Admin Role Permissions  : {admin_perms}")
    print("\n--- Security & Hashability Verification ---")
    
    # 2. Immutability guard
    try:
        read_only.add("execute")
    except AttributeError as e:
        print(f"Immutability Check      : AttributeError caught: {e}")
        
    # 3 & 4. Difference and Dictionary mapping
    elevated_perms = admin_perms - read_only
    print(f"Elevated Capabilities   : {elevated_perms}")
    
    role_mapping = {
        read_only: "Standard Auditor",
        admin_perms: "Root Administrator",
    }
    
    # 5. Hashable key lookup
    role_title = role_mapping[read_only]
    print(f"Dictionary Key Lookup   : Permission profile matches role -> '{role_title}'")

if __name__ == "__main__":
    main()