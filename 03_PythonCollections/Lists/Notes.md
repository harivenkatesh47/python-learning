**Lists in Python - Core Concepts**

**1. Introduction to Lists**
* Lists are ordered, mutable, and heterogeneous collections of elements enclosed in square brackets `[]`[cite: 1].
* Elements can be modified, added, or removed in place without creating a new object in memory[cite: 1].
* A single list can simultaneously store multiple data types, such as integers, strings, and bool eans[cite: 1].

**2. Sequence Operations & Element Insertion**
* Lists use zero-based and negative indexing, with slicing syntax formatted as `list[start:stop:step]`[cite: 1].
* The `+` operator merges two distinct lists, while the `*` operator multiplies elements by an integer factor[cite: 1].
* `.append()` adds an element to the end, `.insert()` places it at a target, and `.extend()` adds items from an iterable individually to the end[cite: 1].

**3. Removal, Search & Ordering**
* `.remove()` deletes a specific value's first occurrence, whereas `.pop()` removes and returns the item at a given index[cite: 1].
* The `in` and `not in` operators evaluate existence, and `.count()` calculates total occurrences[cite: 1].
* `.reverse()` inverts the list, and `.sort()` arranges it in ascending or descending order[cite: 1].

**4. Numerical Aggregations & Nested Lists**
* Built-in functions like `sum()`, `min()`, `max()`, and `len()` compute totals, extremes, and element counts[cite: 1].
* Lists can contain other child lists to form multi-dimensional grids or matrices[cite: 1].
* Nested elements are accessed and mutated using chained bracket notation, such as `matrix[row][col]`[cite: 1].