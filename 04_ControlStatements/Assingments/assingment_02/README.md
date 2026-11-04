# Assignment 2: Control Structures & Applied Logic

## Overview
This assignment deepens the application of logical expressions, operator precedence, and arithmetic safeguards. We are building an academic scholarship evaluator and a smart bill-splitting calculator to enforce strict data validation and computation rules.

## Core Terms & Concepts Explained
* **Operator Precedence:** Using parentheses `()` to explicitly group compound boolean logic (e.g., `((A and B) or C) and D`) to enforce the exact order of evaluation[cite: 1, 2].
* **Floor Division (`//`):** Performs division and rounds down to the nearest whole integer, useful for extracting whole currency units[cite: 1, 2].
* **Modulus (`%`):** Calculates the remainder of a division operation, used here to extract fractional currency subunits (cents)[cite: 1, 2].
* **Boolean Parsing & Type Casting:** Converting raw user string inputs (like "yes" or "no") into strict `True` or `False` boolean states for reliable logic evaluation[cite: 1, 2].

## Task Breakdown
**Task 1: Scholarship & Admission Eligibility Evaluator (`task1_eligibility_evaluator.py`)**
We evaluate student admission tiers. The script takes academic scores and community service verification, combining them into a strict boolean expression with enforced precedence to determine if the student qualifies for a full scholarship, partial admission, or is denied[cite: 1, 2].

**Task 2: Smart Currency & Bill Splitter (`task2_smart_bill_splitter.py`)**
We build a robust financial calculator. The script takes a total bill and participant count, uses comparison operators (`> 0`) to actively prevent division-by-zero errors, rounds the exact share to two decimal places, and extracts the whole dollars and remaining cents using floor division and modulus[cite: 1, 2].