# Module 03: Lists in Python - Revision Notes

## 1. Introduction to Lists
- **Definition:** Ordered, mutable, and heterogeneous collections of elements enclosed in square brackets `[]`[cite: 1].
- **Mutability:** Elements can be modified, added, or removed in place without creating a new object in memory[cite: 1].

## 2. Sequence Operations & Manipulation
- **Slicing & Indexing:** Uses zero-based and negative indexing with `list[start:stop:step]` syntax to return a sublist[cite: 1].
- **Concatenation & Repetition:** `+` merges two distinct lists, while `*` multiplies sequence elements by an integer factor[cite: 1].
- **Element Insertion:** `.append(item)` adds to the end, `.insert(index, item)` places at a designated target, and `.extend(iterable)` appends elements individually[cite: 1].

## 3. Removal, Search & Ordering
- **Extraction:** `.remove(val)` deletes a specific value's first occurrence, whereas `.pop(index)` removes and returns the item at a specified index[cite: 1].
- **Membership & Frequency:** `in` and `not in` evaluate existence, while `.count(val)` returns the total occurrences of an item[cite: 1].
- **Ordering:** `.reverse()` inverts list elements in place; `.sort()` arranges elements in ascending or descending order[cite: 1].

## 4. Numerical Aggregations & Nested Lists
- **Numeric Built-ins:** `sum()`, `min()`, `max()`, and `len()` compute totals, extremes, and element counts[cite: 1].
- **Multi-Dimensional Sequences:** Lists containing other lists form matrices or grids[cite: 1].
- *Example:* `matrix[row][col]` navigates nested dimensions using chained index brackets[cite: 1].