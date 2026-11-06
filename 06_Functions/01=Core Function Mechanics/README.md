# Functions (Part 1): Core Function Mechanics - Core Notes

## 1. Introduction to Functions & Modular Programming
* **Definition of a Function:** A named, reusable block of organized statements written to perform a specific computational task.
* **The DRY (Don't Repeat Yourself) Principle:** Packaging logic into modular functions avoids redundant code, minimizes bugs, and simplifies updates across the codebase.
* **Definition vs. Invocation:** Defining a function (`def`) merely loads its signature and statement block into memory; execution only occurs when the function is explicitly invoked (called) by name.

## 2. User-Defined Functions
* **Syntax Structure:** Declared using the `def` keyword, followed by the function identifier, a parameter list enclosed in parentheses `()`, and a terminal colon `:`.
* **Statement Blocks:** Function bodies are demarcated strictly through standard 4-space indentation.
* **Naming Conventions:** Function identifiers follow PEP 8 snake_case standards (all lowercase with underscores).

## 3. Return Statements & Value Flow
* **The `return` Statement:** Terminates function execution immediately and transfers control and data back to the calling scope.
* **Default Fallback (`None`):** If a function omits a `return` statement or uses an empty `return`, Python implicitly returns `None`.
* **Multiple Return Values:** Separating multiple expressions with commas (e.g., `return a, b, c`) causes Python to automatically pack the values into an immutable `tuple`. The caller can subsequently unpack them directly into individual variables (`x, y, z = func()`).

## 4. Docstrings (PEP 257) & Introspection
* **Docstring Placement:** A string literal written using triple quotes (`"""..."""`) placed as the first line of the function body.
* **Purpose:** Standardizes inline documentation detailing the function's purpose, input parameters, expected types, return types, and potential exceptions.
* **Runtime Introspection:** Docstrings can be inspected programmatically using the `function_name.__doc__` attribute or rendered interactively using `help(function_name)`.