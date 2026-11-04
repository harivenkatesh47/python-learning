# Module 03: Sets - Revision Notes

## 1. Introduction to Sets
- **Definition:** Unordered, unindexed collections of unique, hashable elements enclosed in curly braces `{}`.
- **Deduplication:** Converting a sequence to a set automatically removes duplicate entries.

## 2. Set Mutations
- **Addition & Removal:** `.add(item)` inserts an element, `.remove(item)` deletes it (raising a `KeyError` if absent), and `.discard(item)` fails silently if the item does not exist.

## 3. Mathematical Set Algebra
- **Union (`|`):** Merges elements from both sets.
- **Intersection (`&`):** Retains only elements present in both sets simultaneously.
- **Difference (`-`):** Retains elements present in the primary set but absent from the secondary set.
- **Symmetric Difference (`^`):** Retains elements in either set, but not in both.

## 4. Frozen Sets
- **Definition:** `frozenset()` creates an immutable variant of a set.
- *Example:* Because it cannot be altered after creation, a frozen set is hashable and can be used as a dictionary key.