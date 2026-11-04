# Module 02: Strings in Python - Revision Notes

## 1. String Slicing & Indexing
- **Index Mechanics:** Python uses zero-based indexing (`0` to `len - 1`) from the left and negative indexing (`-1` down to `-len`) from the right.
- **Syntax:** `string[start:stop:step]`.
- *Example:* `text[::-1]` traverses backward, reversing the string (used for palindrome checks).

## 2. Formatting & Escape Sequences
- **f-strings:** Prefixed with `f` or `F`, allowing dynamic insertion and inline evaluation of expressions inside `{}` braces.
- **Escape Sequences:** Special control character sequences preceded by a backslash (`\`).
  - *Example:* `\n` inserts a newline, `\t` inserts a tab, and `\"` inserts literal quotes.

## 3. Boundary & Membership Validation
- **Membership Testing:** `in` and `not in` evaluate whether a target substring exists inside a string, returning a boolean.
- **Boundary Checks:** `.startswith(prefix)` and `.endswith(suffix)` return `True` if the string begins or terminates with the specified pattern.

## 4. Sanitation, Modification & Inspection
- **Whitespace Trimming:** `.strip()` strips all leading and trailing whitespace.
- **Case Transformations:** `.lower()`, `.upper()`, and `.title()` convert alphabetic characters for standardization.
- **Search & Replace:** `.count(sub)` calculates total occurrences, while `.replace(old, new)` returns a new string with substituted values.