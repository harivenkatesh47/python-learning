# Task 1: Scholarship & Admission Eligibility Evaluator

try:
    # 1. Inputs
    applicant_name = input("Enter applicant's name: ").strip()
    academic_score = float(input("Enter high school academic percentage: "))
    entrance_score = float(input("Enter entrance exam score: "))
    
    # 2. Community service input and boolean conversion
    service_input = input("Involved in community service? (yes/no): ").strip().lower()
    has_community_service = (service_input == "yes")
    
    # 3. Compound logical evaluations enforcing precedence with parentheses
    # Primary qualification condition:
    qualifies_academics = ((academic_score >= 85.0) and (entrance_score >= 80.0)) or (academic_score >= 95.0)
    
    # 4. Control flow
    print(f"\n--- Evaluation for {applicant_name} ---")
    if qualifies_academics and has_community_service:
        # High academic threshold with community service gets full scholarship
        if academic_score >= 90.0 or entrance_score >= 85.0:
            print("Status: Full Scholarship")
        else:
            print("Status: Partial Admission")
    elif qualifies_academics and not has_community_service:
        # Meets academics but lacks required service
        print("Status: Partial Admission")
    else:
        print("Status: Application Denied")

except ValueError:
    print("Error: Invalid numeric input. Please enter valid numbers for scores.")