"""
Task 1: Student Exam Score Analytics Engine
Module: Module 05 - Lists in Python
"""

def main():
    print("=== Classroom Grade Analytics ===")
    
    # 1. Initialize numerical scores
    scores = [78, 92, 45, 88, 64, 92, 73, 81, 56, 92]
    total_submissions = len(scores)
    
    print(f"Raw Scores Batch      : {scores}")
    print(f"Total Submissions     : {total_submissions}")
    
    # 2 & 3. Built-in aggregations (min, max, average)
    lowest_score = min(scores)
    highest_score = max(scores)
    class_average = round(sum(scores) / total_submissions, 2)
    
    # 4. Target count
    top_score_frequency = scores.count(highest_score)
    
    print(f"Lowest Score          : {lowest_score}")
    print(f"Highest Score         : {highest_score}")
    print(f"Top Score Frequency   : {top_score_frequency} student(s)")
    print(f"Class Arithmetic Mean : {class_average}")
    
    # 5 & 6. In-place sorting and reversing
    print("\n--- Sorted Distributions ---")
    
    scores.sort()
    print(f"Ascending Rank  : {scores}")
    
    scores.sort(reverse=True)
    print(f"Descending Rank : {scores}")
    
    scores.reverse()
    print(f"Inverted Order  : {scores}")

if __name__ == "__main__":
    main()