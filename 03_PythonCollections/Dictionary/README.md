# Module 03: Dictionaries - Revision Notes

## 1. Introduction to Dictionaries
- **Definition:** Mutable mappings of unique, hashable keys to specific values, enclosed in curly braces `{key: value}`[cite: 1].
- **Key Constraints:** Keys must be immutable (like strings, numbers, or tuples); mutable types cannot be keys[cite: 1].

## 2. CRUD Operations
- **Insertion/Update:** Assign values directly via `d[key] = value` or in bulk using `d.update({key: value})`[cite: 1].
- **Safe Extraction:** Use `.get(key, fallback)` to retrieve values safely without triggering a `KeyError`[cite: 1].
- **Deletion:** `del d[key]` deletes directly, while `d.pop(key)` removes a pair and returns its value[cite: 1].

## 3. Dictionary Views & Memory Mechanics
- **Views:** `.keys()` returns keys, `.values()` returns values, and `.items()` returns key-value tuple pairs[cite: 1].
- **Shallow Copy:** `.copy()` duplicates the top container, but nested mutable objects still reference original memory addresses[cite: 1].
- **Deep Copy:** `copy.deepcopy()` recursively clones the entire object graph, constructing fully independent copies to avoid side-effect mutations[cite: 1].