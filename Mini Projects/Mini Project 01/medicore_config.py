total_patients_served = 0
clinic_status = "OPEN"

triage_queue = ["PT-1001 | Aarav Patel | ROUTINE"]
consultation_durations = [10, 15,25,30,45]
daily_invoices = [450.50, 1280.00 , 310.75, 600.00, 1500.25]

icu_bed_matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

bed_assignments = {
    (0,0): "PT-901 (Post-Op)",
    (0,2): "PT-902 (Critical Care)",
    (1,1): "PT-903 (ICU)",
    (2,0): "PT-904 (Recovery)",
    (2,1): "PT-905 (Observation)"
}    

pharmacy_catalog = {
    "paracetamol": {
        "price": 45.0,
        "stock": 25,
        "ingredients": {"acetaminophen", "starch"}
    },
    "amoxicillin": {
        "price": 120.0,
        "stock": 15,
        "ingredients": {"amoxicillin trihydrate", "magnesium stearate"}
    },
    "ibuprofen": {
        "price": 60.0,
        "stock": 30,
        "ingredients": {"ibuprofen", "lactose"}
    },
    "omeprazole": {
        "price": 150.0,
        "stock": 10,
        "ingredients": {"omeprazole magnesium", "microcrystalline cellulose"}
    },
}

basic_tier_rules = frozenset(["OPD","GENERIC_MEDS"])
premium_tier_rules = frozenset(["OPD","GENERIC_MEDS","ICU_COVER","SURGERY"])

insurance_policy_registry = {
    basic_tier_rules:"Standard CGHS Tier",
    premium_tier_rules:"Platinum Corporate Cover"
}

department_hierarchy = {
    "dept": "General Medicine",
    "lead": "Dr. K. Verma",
    "conditions": ["fever", "flu", "fatigue"],
    "sub_units": [
        {
            "dept": "Cardiology",
            "lead": "Dr. R. Nair",
            "conditions": ["arrhythmia", "hypertension"],
            "sub_units": [
                {
                    "dept": "Interventional Electrophysiology",
                    "lead": "Dr. S. Iyer",
                    "conditions": ["pacemaker_fault", "atrial_fibrillation"],
                    "sub_units": []
                }
            ]
        },
        {
            "dept": "Pulmonology",
            "lead": "Dr. A. Khan",
            "conditions": ["asthma", "bronchitis"],
            "sub_units": [
                {
                    "dept": "Critical Care Respiratory",
                    "lead": "Dr. M. Das",
                    "conditions": ["acute_hypoxia", "ARDS"],
                    "sub_units": []
                }
            ]
        }
    ]
}    

if __name__ == "__main__":
    print("=== Medicore Config Self-Test ===")
    print(f"Module Execution Name : {__name__}")
    print(f"Catalog Drugs Loaded : {len(pharmacy_catalog)}")
    print(F"Initial Queue Count : {len(triage_queue)}")
    print(f"Policy Lookup Test : {insurance_policy_registry[basic_tier_rules]}")
