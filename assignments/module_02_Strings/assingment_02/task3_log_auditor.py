"""
Task 3: Security Log Threat Auditor
Author: Hari Venkatesh
Module: Module 02 - Strings in Python
"""

def main():
    print("=== Server Log Auditor ===")
    raw_log = input("Enter raw log: ").strip()

    # 1. Verify log framing with startswith
    begins_valid = raw_log.startswith("WARN") or raw_log.startswith("ERROR")
    initial_state = (
        "Begins with recognized alert flag"
        if begins_valid
        else "Unrecognized log prefix"
    )

    # 2. Measure alert occurrences
    warn_count = raw_log.count("WARN")

    # 3. Transform to uppercase and replace alerts with standardized tags
    upper_log = raw_log.upper()
    redacted_payload = upper_log.replace("WARN", "[ALERT-LVL-2]")

    # 4. Multiline output utilizing escaped quotes (\") and backslashes (\\)
    system_path = "C:\\logs\\security_audit.txt"

    print("\n--- Security Audit Output ---")
    print(f"Initial State : {initial_state}")
    print(f"Alert Count   : {warn_count} instance(s) found")
    print(f"Final Payload : \"{redacted_payload}\"")
    print(f"System Path   : {system_path}")


if __name__ == "__main__":
    main()