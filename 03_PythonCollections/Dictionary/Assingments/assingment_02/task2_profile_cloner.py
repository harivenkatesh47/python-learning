"""
Task 2: Cloud Profile Cloner (Shallow vs Deep Copy)
"""

import copy

def main():
    print("=== Cloud Profile Memory Replication Audit ===")
    
    # 2. Setup baseline
    base_profile = {
        "cluster_id": "clus-east-01",
        "specs": {"cpu": 4, "ram": 16},
    }
    print(f"Original Initial Specs: {base_profile['specs']}")
    
    # 3 & 4. Clone generation
    shallow_profile = base_profile.copy()
    deep_profile = copy.deepcopy(base_profile)
    
    print("\n--- Performing Mutations ---")
    # 5 & 6. Deep mutations
    shallow_profile["specs"]["cpu"] = 8
    print("Altered shallow_profile nested CPU to 8")
    
    deep_profile["specs"]["ram"] = 64
    print("Altered deep_profile nested RAM to 64")
    
    # 7 & 8. Prove memory architecture
    print("\n--- Inspection of Objects in Memory ---")
    print(f"Base Profile (Original) : {base_profile}")
    print(f"Shallow Copy Profile    : {shallow_profile}")
    print(f"Deep Copy Profile       : {deep_profile}")
    
    print("\nVerification Verdict:")
    print(f"Shallow copy impacted base profile specs (Shared Reference: {base_profile['specs']['cpu'] == shallow_profile['specs']['cpu']})")
    print(f"Deep copy isolated base profile specs (Independent Memory: {base_profile['specs']['ram'] != deep_profile['specs']['ram']})")

if __name__ == "__main__":
    main()