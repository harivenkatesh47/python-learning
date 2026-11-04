# Module 03: Tuples - Revision Notes

## 1. Introduction to Tuples
- **Definition:** Ordered, immutable collections of elements enclosed in parentheses `()`[cite: 1].
- **Immutability:** Once created, elements cannot be reassigned, appended, or deleted in place; attempts to mutate raise a `TypeError`[cite: 1].
- *Example:* A single-element tuple requires a trailing comma (e.g., `(item,)`) to distinguish it syntactically from an expression[cite: 1].

## 2. Sequence Operations & Inspection
- **Slicing & Operations:** Tuples support zero-based indexing, slicing, concatenation (`+`), and repetition (`*`)[cite: 1].
- **Inspection:** `.count(value)` returns the frequency of an item, and `.index(value)` locates its first occurrence[cite: 1].
- **Dictionary Keys:** Because tuples are strictly immutable and hashable, they can safely be used as dictionary keys[cite: 1].