user_cache = ["user_101", "user_102"]
config_state = "STANDARD"

def mutate_cache_in_place(new_user):
    user_cache.append(new_user)
    print(f"Mutated Cache In-Place : {user_cache}")

def reassign_cache_reference(new_cache_list):
    global user_cache
    user_cache = new_cache_list
    print(f"Reassigned Global Cache: {user_cache}")

def update_config_state(new_state):
    global config_state
    config_state = new_state
    print(f"Updated Config State   : {config_state}")

def main():
    print("=== Shared Cache Mutation vs Reassignment ===")
    print(f"Initial Cache : {user_cache}")
    print(f"Initial Config: {config_state}")
    
    print("\n--- Applying In-Place Mutation (No global keyword) ---")
    mutate_cache_in_place("user_103")
    
    print("\n--- Reassigning Global Reference (Requires global keyword) ---")
    reassign_cache_reference(["admin_01", "admin_02"])
    
    print("\n--- Reassigning Immutable Variable (Requires global keyword) ---")
    update_config_state("ELEVATED")

if __name__ == "__main__":
    main()