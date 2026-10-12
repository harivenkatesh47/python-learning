# Assignment 1: String Parsing, Slicing & Boundary Analysis

## Learning Objectives
* Demonstrate slicing syntax (`[start:stop:step]`) to extract substrings and reverse characters.
* Validate string prefixes and suffixes using `.startswith()` and `.endswith()`.
* Check pattern existence using the `in` membership operator.
* Format structured console output using f-strings and escape sequences (`\n`, `\t`).

## Task 1: Web Endpoint & Protocol Inspector
Write a script named `task1_url_inspector.py` that inspects a raw endpoint URL entered by a user, verifies whether it meets protocol and domain criteria, and slices out the core components.
1. Prompt the user for a web URL and remove accidental leading/trailing whitespace using `.strip()`.
2. Convert the string to lowercase using `.lower()` for uniform evaluation.
3. Check whether the URL begins with `https://` using `.startswith()`. If it starts with `http://`, warn the user of an insecure connection; otherwise, flag it as invalid.
4. Verify if the URL ends with a valid top-level domain (`.com`, `.org`, or `.net`) using `.endswith()`.
5. Check if `api` is present in the URL using the `in` membership operator to check for API endpoints.
6. Using string slicing: Extract the protocol and the domain name without the protocol prefix.
7. Print an inspection report using f-strings, utilizing `\t` for indentation and `\"` to enclose the extracted domain in quotes.

## Task 2: Encrypted Token Decrypter & Palindrome Validator
Write a script named `task2_token_decoder.py` that processes a raw data packet token, isolates its internal security payload using step slicing, and checks whether the payload is symmetric (a palindrome).
1. Prompt the user for an alphanumeric token string.
2. Clean leading/trailing spaces with `.strip()`.
3. Verify that the token begins with `TK-` using `.startswith()`.
4. Using string slicing: Slice out the central payload (from index 3 up to index -3) and create a reversed copy of the payload using reverse step slicing (`[::-1]`).
5. Compare the extracted payload with its reversed version using the `==` comparison operator to determine if it is a palindrome.
6. Print the decrypted results, original slice, and symmetry status using f-strings and multiline formatting with `\n`.