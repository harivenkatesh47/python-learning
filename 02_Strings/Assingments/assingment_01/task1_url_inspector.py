"""
Task 1: Web Endpoint & Protocol Inspector
Author: Hari Venkatesh
Module: Module 02 - Strings in Python
"""

def main():
    print("=== Web Endpoint Inspector ===")
    raw_url = input("Enter URL: ")

    # 1. Clean accidental whitespace and standardize case
    clean_url = raw_url.strip().lower()

    # 2. Check protocol and SSL security
    is_secure = clean_url.startswith("https://")
    is_http = clean_url.startswith("http://")

    if is_secure:
        protocol = "https"
    elif is_http:
        protocol = "http"
        print("[Warning]: Insecure connection detected (HTTP).")
    else:
        protocol = "unknown"
        print("[Warning]: Invalid or missing HTTP/HTTPS protocol.")

    # 3. Check for valid Top-Level Domain (TLD)
    valid_tld = clean_url.endswith((".com", ".org", ".net"))

    # 4. Check API endpoint status using membership operator
    is_api = "api" in clean_url

    # 5. Extract domain using slicing
    if is_secure:
        clean_target = clean_url[8:]   # len("https://") == 8
    elif is_http:
        clean_target = clean_url[7:]   # len("http://") == 7
    else:
        clean_target = clean_url

    # 6. Format output using f-strings and escape sequences (\t, \")
    print("\n--- Analysis Report ---")
    print(f"\tProtocol      : {protocol}")
    print(f"\tSecure (SSL)  : {is_secure}")
    print(f"\tAPI Endpoint  : {is_api}")
    print(f"\tValid TLD     : {valid_tld}")
    print(f"\tClean Target  : \"{clean_target}\"")


if __name__ == "__main__":
    main()