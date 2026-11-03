"""
Task 1: Server Fleet Hardware Registry
"""

def main():
    print("=== Server Fleet Hardware Registry ===")
    
    # 1. Initialize
    server = {
        "hostname": "prod-api-01",
        "ip": "192.168.1.100",
        "cores": 8,
        "ram_gb": 32,
        "status": "active",
    }
    print(f"Initial Server Loaded: {server['hostname']}")
    print("\n--- Modifications Executed ---")
    
    # 2 & 3. Mutations
    server["ram_gb"] = 64
    server.update({"status": "maintenance", "region": "ap-south-1"})
    print(f"RAM Allocated        : {server['ram_gb']} GB")
    print(f"Status & Region Set  : {server['status']}, {server['region']}")
    
    # 4 & 5. Safe deletions
    removed_ip = server.pop("ip")
    del server["cores"]
    print(f"Decommissioned IP    : {removed_ip}")
    
    # 6. Fallback getter
    cores_fallback = server.get("cores", "Not Configured")
    print(f"Safe Fallback Read   : Cores -> {cores_fallback}")
    
    # 7. Views
    print("\n--- Current Registry State ---")
    print(f"Remaining Keys       : {server.keys()}")
    print(f"Active Values        : {server.values()}")
    print("Formatted Key-Values :")
    for key, val in server.items():
        print(f"\t{key} : {val}")

if __name__ == "__main__":
    main()