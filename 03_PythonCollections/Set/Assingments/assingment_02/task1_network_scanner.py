"""
Task 1: Security Network Vulnerability Scanner
"""

def main():
    print("=== Network Vulnerability Cross-Audit ===")
    
    scanner_a = {"CVE-101", "CVE-102", "CVE-105", "CVE-109"}
    scanner_b = {"CVE-102", "CVE-105", "CVE-110", "CVE-112"}
    
    print(f"Scanner A Findings : {scanner_a}")
    print(f"Scanner B Findings : {scanner_b}")
    print("\n--- Set Algebra Analysis ---")
    
    # Mathematical set operations
    union_set = scanner_a | scanner_b
    intersection_set = scanner_a & scanner_b
    diff_set = scanner_a - scanner_b
    sym_diff_set = scanner_a ^ scanner_b
    
    print(f"All Unique Threats (Union |)            : {union_set}")
    print(f"Confirmed Overlap (Intersection &)      : {intersection_set}")
    print(f"Scanner A Exclusive Flaws (Difference -): {diff_set}")
    print(f"Uncorrelated Alerts (Symmetric Diff ^)  : {sym_diff_set}")

if __name__ == "__main__":
    main()