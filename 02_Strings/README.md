# Module 02: Strings in Python - Revision Notes

## 1. String Slicing & Indexing
- **Index Mechanics:** Python uses zero-based indexing (`0` to `len - 1`) from the left and negative indexing (`-1` down to `-len`) from the right[cite: 1].
- **Syntax:** `string[start:stop:step]`[cite: 1].
- *Example:* `text[::-1]` traverses backward, reversing the string (used for palindrome checks)[cite: 1].

## 2. Formatting & Escape Sequences
- **f-strings:** Prefixed with `f` or `F`, allowing dynamic insertion and inline evaluation of expressions inside `{}` braces[cite: 1].
- **Escape Sequences:** Special control character sequences preceded by a backslash (`\`)[cite: 1].
  - *Example:* `\n` inserts a newline, `\t` inserts a tab, and `\"` inserts literal quotes[cite: 1].

## 3. Boundary & Membership Validation
- **Membership Testing:** `in` and `not in` evaluate whether a target substring exists inside a string, returning a boolean[cite: 1].
- **Boundary Checks:** `.startswith(prefix)` and `.endswith(suffix)` return `True` if the string begins or terminates with the specified pattern[cite: 1].

## 4. Sanitation, Modification & Inspection
- **Whitespace Trimming:** `.strip()` strips all leading and trailing whitespace[cite: 1].
- **Case Transformations:** `.lower()`, `.upper()`, and `.title()` convert alphabetic characters for standardization[cite: 1].
- **Search & Replace:** `.count(sub)` calculates total occurrences, while `.replace(old, new)` returns a new string with substituted values[cite: 1].