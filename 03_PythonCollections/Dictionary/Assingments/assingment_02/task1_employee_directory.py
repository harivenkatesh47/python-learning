"""
Task 1: Multi-Department Employee Directory
"""

def main():
    print("=== Enterprise Department Directory ===")
    
    # 1. Nested setup
    organization = {
        "engineering": {
            "lead": "Hari",
            "headcount": 14,
            "technologies": ["Python", "Docker", "PostgreSQL"],
        },
        "operations": {
            "lead": "Priya",
            "headcount": 6,
            "technologies": ["Linux", "Bash"],
        },
    }
    
    # 2. Extract nested node
    eng_lead = organization["engineering"]["lead"]
    print(f"Engineering Team Lead : {eng_lead}")
    print("\n--- Updating Operational Records ---")
    
    # 3, 4 & 5. Deep mutations
    organization["engineering"]["technologies"].append("FastAPI")
    organization["operations"]["headcount"] += 2
    organization.update({
        "marketing": {
            "lead": "Suresh",
            "headcount": 4,
            "technologies": ["SEO", "Analytics"]
        }
    })
    
    print(f"Appended Tech (Eng)   : {organization['engineering']['technologies']}")
    print(f"Updated Ops Headcount : {organization['operations']['headcount']}")
    print(f"Registered Departments: {list(organization.keys())}")
    
    print("\n--- Complete Directory State ---")
    for dept, data in organization.items():
        print(f"{dept:<11} -> Lead: {data['lead']} | Headcount: {data['headcount']} | Tech: {data['technologies']}")

if __name__ == "__main__":
    main()