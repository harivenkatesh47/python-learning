# Module 01: Python Basics - Revision Notes

## 1. Core Elements
- **Literals:** Raw, hardcoded data values entered directly into the source code (e.g., `10`, `3.14`, `"Hello"`)[cite: 1].
- **Variables:** Named memory references used as containers to store, label, and retrieve data values across program execution[cite: 1].
- **Keywords:** Reserved identifiers built directly into Python (e.g., `if`, `def`, `True`) that carry strict syntax meanings and cannot be repurposed as variable names[cite: 1].

## 2. Primitive Datatypes & Conversion
- **Types:** Integers (`int`), Decimals (`float`), Text (`str`), and Booleans (`bool`)[cite: 1].
- **Type Casting:** Explicitly converting data[cite: 1]. 
  - *Example:* `float(input())` explicitly converts string representations of numbers into numeric types for computation[cite: 1].
  - *Boolean casting:* `bool(val)` evaluates to `False` for `0`, `None`, and empty sequences, and `True` for non-zero values[cite: 1].

## 3. Operators & Precedence
- **Arithmetic:** `+` (add), `-` (subtract), `*` (multiply), `/` (true float division), `//` (floor division), `%` (modulus), `**` (exponent)[cite: 1].
- **Comparison:** `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`. Return `True` or `False`[cite: 1].
- **Logical:** `and`, `or`, `not`[cite: 1].
- **Precedence:** Governs the evaluation sequence of operations (Parentheses → Exponentiation → Multiplication/Division/Modulus → Addition/Subtraction → Comparisons → Logical)[cite: 1].

## 4. Input & Output
- **Console Output:** `print()` writes data strings to the standard console and supports formatted strings[cite: 1].
- **Console Input:** `input()` halts program execution to read a line from standard input, always returning the captured data as a string[cite: 1].