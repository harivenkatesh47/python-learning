"""
Task 2: Encrypted Token Decrypter & Palindrome Validator
Author: Hari Venkatesh
Module: Module 02 - Strings in Python
"""

def main():
    print("=== Token Payload Decoder ===")
    raw_token = input("Enter security token: ").strip()

    # 1. Verify prefix
    has_valid_prefix = raw_token.startswith("TK-")
    if not has_valid_prefix:
        print("[Warning]: Token does not begin with standard prefix 'TK-'.")

    # 2. Slice out core payload (drop first 3 chars 'TK-' and last 3 chars '-XX')
    # Example: "TK-RADAR-88" -> starts at index 3, ends before index -3
    extracted_core = raw_token[3:-3]

    # 3. Step slice to reverse payload
    reversed_core = extracted_core[::-1]

    # 4. Palindrome check using equality operator
    is_symmetric = (extracted_core == reversed_core) and (len(extracted_core) > 0)

    # 5. Multiline output via f-strings and escape sequences
    print("\n--- Decoded Payload ---")
    print(f"Raw Token     : {raw_token}\n"
          f"Extracted Core: {extracted_core}\n"
          f"Reversed Core : {reversed_core}\n"
          f"Symmetric Key : {is_symmetric}")


if __name__ == "__main__":
    main()