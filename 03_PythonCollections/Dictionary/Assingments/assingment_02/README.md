# Assignment 2: Dictionaries - Nested Mapping & Memory Mechanics

## Overview
This assignment tackles complex nested hierarchies and memory duplication. We are building a multi-department employee directory and a cloud profile cloner to differentiate between shallow and deep memory copies.

## Core Terms & Concepts Explained
* **Nested Dictionaries:** Dictionaries placed inside other dictionaries to model complex relational hierarchies.
* **Chained Indexing:** Using sequential brackets, like `dict[key1][key2]`, to navigate deep into nested structures.
* **Shallow Copy (`.copy()`):** Duplicates the top-level dictionary, but nested lists or dictionaries still share the same memory reference as the original. Mutating the nested items affects both dictionaries.
* **Deep Copy (`copy.deepcopy()`):** Recursively clones the entire object tree. Nested items get completely independent memory addresses, preventing accidental side effects.

## Task Breakdown
**Task 1: Multi-Department Employee Directory**
We manage a nested corporate org chart. The script navigates deep keys to append technologies, updates headcount numbers in place, and injects a completely new department dictionary using `.update()`.

**Task 2: Cloud Profile Cloner**
We configure infrastructure profiles to test memory leaks. The script mutates nested specs inside both a shallow copy and a deep copy, mathematically proving that the shallow copy alters the original baseline while the deep copy safely isolates changes.