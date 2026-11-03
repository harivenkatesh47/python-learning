**Tuples - Core Concepts**

**1. Introduction to Tuples**
* Tuples are ordered, immutable collections of elements enclosed in parentheses `()`[cite: 1].
* Once created, elements cannot be reassigned, appended, or deleted in place; attempts to mutate raise a `TypeError`[cite: 1].
* A single-element tuple requires a trailing comma (e.g., `(item,)`) to distinguish it from an expression wrapped in parentheses[cite: 1].

**2. Sequence Operations**
* Tuples support zero-based indexing and slicing using `tuple[start:stop:step]`[cite: 1].
* The `+` operator merges tuples via concatenation, and the `*` operator duplicates elements via repetition[cite: 1].
* Tuple unpacking allows assigning elements directly to multiple variables in a single operation (e.g., `lat, lon = coordinates`).

**3. Inspection & Usage**
* `.count(value)` returns the frequency of a specific item, and `.index(value)` locates its first occurrence index[cite: 1].
* The `in` and `not in` operators evaluate membership[cite: 1].
* Because they are strictly immutable and hashable, tuples can safely be used as dictionary keys[cite: 1].