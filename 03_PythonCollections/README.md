# Python Collections - Core Architecture & Comparison

Python provides four primary built-in collection data types used to store groups of items: **Lists**, **Tuples**, **Sets**, and **Dictionaries**.

---

## 1. Comparative Breakdown

| Feature | List | Tuple | Set | Dictionary |
| :--- | :--- | :--- | :--- | :--- |
| **Enclosure** | `[]` Square brackets | `()` Parentheses | `{}` Curly braces | `{key: value}` Key-value pairs |
| **Mutability** | Mutable (In-place changes) | Immutable (Fixed state) | Mutable (Can add/remove) | Mutable (Values & keys) |
| **Ordering** | Ordered (Preserves insertion) | Ordered (Preserves insertion) | Unordered / Unindexed | Insertion-ordered (Python 3.7+) |
| **Indexing / Slicing** | Supported (`list[0:2]`) | Supported (`tuple[0:2]`) | Not supported | Key-based lookup (`dict[key]`) |
| **Duplicates** | Allowed | Allowed | Automatically removed | Keys: Unique | Values: Allowed |
| **Key Use Case** | Dynamic sequential data | Protected, constant records | Deduplication & set algebra | Associative mapping & lookups |

---

## 2. Core Behavior Summary

*   **Lists (`list`):**
    *   Designed for dynamic sequences where items need to be frequently inserted, reordered, or removed.
    *   Key methods: `.append()`, `.insert()`, `.extend()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`.
*   **Tuples (`tuple`):**
    *   Designed for fixed records and constant data where write-protection is required.
    *   Because they are immutable, they are strictly hashable and can be used as dictionary keys.
    *   Key methods: `.count()`, `.index()`.
*   **Sets (`set` & `frozenset`):**
    *   Designed for fast uniqueness checks, automatic deduplication, and mathematical algebra.
    *   Operations: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`).
    *   `frozenset` provides an immutable, hashable alternative that can serve as dictionary keys.
*   **Dictionaries (`dict`):**
    *   Designed for key-value pair data association.
    *   Keys must be unique and immutable; values can be of any data type.
    *   Key methods: `.get()`, `.update()`, `.pop()`, `.keys()`, `.values()`, `.items()`.
    *   Memory copying: Shallow copies (`.copy()`) preserve nested object memory references, while deep copies (`copy.deepcopy()`) duplicate the entire object graph independently.