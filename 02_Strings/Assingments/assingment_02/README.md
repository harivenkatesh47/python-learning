# Assignment 2: Data Cleaning, Sanitation & Text Metrics

## Learning Objectives
* Clean and normalize raw user text using `.strip()` and case manipulation (`.upper()`, `.lower()`, `.title()`).
* Replace targeted substrings dynamically using `.replace()`.
* Compute substring frequency using `.count()`.
* Handle quote formatting and layout alignment using escape sequences (`\n`, `\t`, `\"`, `\'`).

## Task 1: Clinical Note Sanitizer & Redactor
Write a script named `task1_text_sanitizer.py` that takes an unstructured medical record snippet, standardizes casing, replaces protected health information (PHI) with redacted tags, and counts the occurrences of key audit terms.
1. Prompt the user to enter a medical record entry and a sensitive word/name to redact.
2. Remove outer whitespace from both inputs using `.strip()`.
3. Count how many times the sensitive word appears in the entry using `.count()` (perform a case-insensitive check by comparing lowercase copies).
4. Replace all occurrences of the sensitive word with `[CONFIDENTIAL]` using `.replace()`.
5. Format the patient's record by transforming the header to uppercase (`.upper()`).
6. Output a summary using an f-string showing the count of redacted words and the sanitized text enclosed in escape characters (`\"`).

## Task 2: Resume Header & Title Formatter
Write a script named `task2_resume_formatter.py` that accepts an unformatted contact line from a candidate's resume, standardizes its casing, replaces custom delimiters, and formats an export-ready profile header.
1. Prompt the user for a candidate line in the format: `name | current role | location`.
2. Clean unnecessary edge whitespace using `.strip()`.
3. Check for the delimiter `|` using the `in` membership operator. If missing, notify the user.
4. Transform the entire string to Title Case using `.title()` so that every word begins with a capital letter.
5. Replace every instance of the pipe delimiter `|` with an arrow symbol `->` using `.replace()`.
6. Count how many sections were separated by counting the occurrences of `->`.
7. Display the formatted string on a new line using `\n` and tabbed layout (`\t`).

## Task 3: Security Log Threat Auditor
Write a script named `task3_log_auditor.py` that processes a server event log string, detects critical error keywords, replaces warning flags with standardized tags, and verifies log framing.