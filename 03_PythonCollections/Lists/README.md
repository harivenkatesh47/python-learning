# Module 03: Lists in Python - Revision Notes

## 1. Introduction to Lists
- **Definition:** Ordered, mutable, and heterogeneous collections of elements enclosed in square brackets `[]`.
- **Mutability:** Elements can be modified, added, or removed in place without creating a new object in memory.

## 2. Sequence Operations & Manipulation
- **Slicing & Indexing:** Uses zero-based and negative indexing with `list[start:stop:step]` syntax to return a sublist.
- **Concatenation & Repetition:** `+` merges two distinct lists, while `*` multiplies sequence elements by an integer factor.
- **Element Insertion:** `.append(item)` adds to the end, `.insert(index, item)` places at a designated target, and `.extend(iterable)` appends elements individually.

## 3. Removal, Search & Ordering
- **Extraction:** `.remove(val)` deletes a specific value's first occurrence, whereas `.pop(index)` removes and returns the item at a specified index.
- **Membership & Frequency:** `in` and `not in` evaluate existence, while `.count(val)` returns the total occurrences of an item.
- **Ordering:** `.reverse()` inverts list elements in place; `.sort()` arranges elements in ascending or descending order.

## 4. Numerical Aggregations & Nested Lists
- **Numeric Built-ins:** `sum()`, `min()`, `max()`, and `len()` compute totals, extremes, and element counts.
- **Multi-Dimensional Sequences:** Lists containing other lists form matrices or grids.
- *Example:* `matrix[row][col]` navigates nested dimensions using chained index brackets.