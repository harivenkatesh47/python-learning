"""
Task 1: Academic Roster Ledger
"""

def main():
    print("=== Academic Record Processor ===")
    
    # 1. Nested tuple
    roster = (
        ("Alice", (85, 90, 88)),
        ("Bob", (72, 68, 75)),
        ("Charlie", (95, 92, 98)),
    )
    
    # 2. Multi-dimensional indexing
    charlie_exam2 = roster[2][1][1]
    print(f"Direct Multi-Index Sample (Charlie, Exam 2) : {charlie_exam2}")
    print("\n--- Student Performance Breakdown ---")
    
    # 3. Aggregations
    for student, scores in roster:
        print(f"{student:7} : Total = {sum(scores)}, Min = {min(scores)}, Max = {max(scores)}")
        
    # 4. Data conversion and mutation
    bob_record = roster[1]
    bob_scores_list = list(bob_record[1])
    bob_scores_list[1] = 74
    corrected_bob_record = (bob_record[0], tuple(bob_scores_list))
    
    print("\n--- Grade Correction Applied ---")
    print(f"Original Bob Record : {bob_record}")
    print(f"Corrected Record    : {corrected_bob_record}")

if __name__ == "__main__":
    main()