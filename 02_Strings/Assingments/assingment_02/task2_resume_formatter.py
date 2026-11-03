"""
Task 2: Resume Header & Title Formatter
Author: Hari Venkatesh
Module: Module 02 - Strings in Python
"""

def main():
    print("=== Resume Header Formatter ===")
    raw_info = input("Enter raw profile info: ").strip()

    # 1. Check delimiter existence
    if "|" not in raw_info:
        print("[Error]: Input missing standard pipe '|' delimiter.")
        return

    # 2. Apply Title Case to normalize every word
    titled_info = raw_info.title()

    # 3. Replace pipe delimiter with arrow format
    formatted_profile = titled_info.replace(" | ", " -> ").replace("|", " -> ")

    # 4. Count segments by counting delimiter arrows + 1
    arrow_count = formatted_profile.count("->")
    segment_count = arrow_count + 1

    # 5. Output with newline (\n) and tab (\t) formatting
    print("\n--- Formatted Profile ---")
    print(f"\tProfile : {formatted_profile}")
    print(f"\tSegments: {segment_count}")


if __name__ == "__main__":
    main()