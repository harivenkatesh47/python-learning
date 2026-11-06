def main():
    print("=== Functional Data Processing Pipeline ===")
    
    raw_scores = [102, 45, 78, -12, 88, 62, 115, 95, 33, 74]
    print(f"Raw Input Batch       : {raw_scores}")
    
    # Stage 1: Validation Filter
    valid_scores = list(filter(lambda x: 0 <= x <= 100, raw_scores))
    
    # Stage 2: Passing Filter
    passing_cohort = list(filter(lambda x: x >= 60, valid_scores))
    
    # Stage 3: Transformation Map
    transformed_stream = list(map(
        lambda score: f"{score}% -> PASS (Grade: {'A' if score >= 85 else 'B' if score >= 70 else 'C'})", 
        passing_cohort
    ))
    
    print("\n--- Pipeline Progression ---")
    print(f"Valid Scores Filtered : {valid_scores}")
    print(f"Passing Cohort (>= 60): {passing_cohort}")
    
    print("\n--- Transformed Output Stream (map) ---")
    for output in transformed_stream:
        print(f"\t* {output}")

if __name__ == "__main__":
    main()