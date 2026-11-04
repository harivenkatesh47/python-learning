# Module 03: Tuples - Revision Notes

## 1. Introduction to Tuples
- **Definition:** Ordered, immutable collections of elements enclosed in parentheses `()`.
- **Immutability:** Once created, elements cannot be reassigned, appended, or deleted in place; attempts to mutate raise a `TypeError`.
- *Example:* A single-element tuple requires a trailing comma (e.g., `(item,)`) to distinguish it syntactically from an expression.

## 2. Sequence Operations & Inspection
- **Slicing & Operations:** Tuples support zero-based indexing, slicing, concatenation (`+`), and repetition (`*`).
- **Inspection:** `.count(value)` returns the frequency of an item, and `.index(value)` locates its first occurrence.
- **Dictionary Keys:** Because tuples are strictly immutable and hashable, they can safely be used as dictionary keys.