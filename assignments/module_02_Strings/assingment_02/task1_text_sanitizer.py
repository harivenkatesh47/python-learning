"""
Task 1: Clinical Note Sanitizer & Redactor
Author: Hari Venkatesh
Module: Module 02 - Strings in Python
"""

def main():
    print("=== Clinical Record Sanitizer ===")
    raw_record = input("Enter record: ").strip()
    sensitive_word = input("Enter word to redact: ").strip()

    # 1. Case-insensitive count using lowercased copies
    record_lower = raw_record.lower()
    word_lower = sensitive_word.lower()
    matches_found = record_lower.count(word_lower)

    # 2. Replace target occurrences with confidentiality tag
    # Direct replacement handling both lowercase and titled instances
    sanitized_note = raw_record.replace(sensitive_word, "[CONFIDENTIAL]")
    if sensitive_word.lower() != sensitive_word:
        sanitized_note = sanitized_note.replace(sensitive_word.lower(), "[CONFIDENTIAL]")
    if sensitive_word.title() != sensitive_word:
        sanitized_note = sanitized_note.replace(sensitive_word.title(), "[CONFIDENTIAL]")

    # 3. Formatted output with escaped quotes (\") and newlines (\n)
    print("\n--- Audit Report ---")
    print(f"Matches Found : {matches_found}")
    print(f"Sanitized Note:\n\"{sanitized_note}\"")


if __name__ == "__main__":
    main()