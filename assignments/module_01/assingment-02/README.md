# Assignment 2: Control Structures & Applied Logic

## Learning Objectives

Demonstrate mastery of relational and logical operators, operator precedence, type conversions, conditional branching (`if`, `elif`, `else`), and input validation.

## Task 1: Scholarship & Admission Eligibility Evaluator

Write a script that:
1. Takes an applicant's name, academic score (percentage as a float), and entrance exam score (float) as inputs.
2. Takes a response for community service involvement (`yes` or `no`) and converts it to a boolean value.
3. Evaluates eligibility using compound logical expressions (`and`, `or`, `not`) with proper parentheses to enforce operator precedence:
* High school percentage $\ge 85.0$ **and** entrance score $\ge 80.0$, **or** high school percentage $\ge 95.0$.
* **And** community service must be `True`.
4. Uses `if-elif-else` control flow to output whether the student is awarded a "Full Scholarship", "Partial Admission", or "Application Denied".
5. Catches non-numeric inputs using a `try-except ValueError` block.


## Task 2: Smart Currency & Bill Splitter

Write a script that:
1. Prompts for the total bill amount (float) and number of people sharing the bill (integer).
2. Uses comparison operators to validate that the number of participants is strictly greater than 0 to prevent division by zero.
3. Computes each person's exact share, rounding to 2 decimal places using the `round()` numeric function.
4. Uses floor division (`//`) and modulus (`%`) to split the share into whole dollars and remaining cents.
5. Formats the breakdown cleanly to the console using f-strings.


## Task 3: Bill Splitting & Currency Breakdown

Write a script that:
1. Prompts the user for the total bill amount (float) and the total number of people sharing the bill (integer).
2. Validates that the number of people is strictly greater than 0 using comparison operators to prevent division by zero.
3. Computes each individual's share, rounded to 2 decimal places using the `round()` numeric function.
4. Uses floor division (`//`) and remainder/modulus (`%`) operators to separate the share into whole currency units (dollars) and remaining fractional units (cents).
5. Catches invalid non-numeric inputs using a `try-except ValueError` block.
6. Outputs a formatted split summary to the console using f-strings.