# Module 03: Sets - Revision Notes

## 1. Introduction to Sets
- **Definition:** Unordered, unindexed collections of unique, hashable elements enclosed in curly braces `{}`[cite: 1].
- **Deduplication:** Converting a sequence to a set automatically removes duplicate entries[cite: 1].

## 2. Set Mutations
- **Addition & Removal:** `.add(item)` inserts an element, `.remove(item)` deletes it (raising a `KeyError` if absent), and `.discard(item)` fails silently if the item does not exist[cite: 1].

## 3. Mathematical Set Algebra
- **Union (`|`):** Merges elements from both sets[cite: 1].
- **Intersection (`&`):** Retains only elements present in both sets simultaneously[cite: 1].
- **Difference (`-`):** Retains elements present in the primary set but absent from the secondary set[cite: 1].
- **Symmetric Difference (`^`):** Retains elements in either set, but not in both[cite: 1].

## 4. Frozen Sets
- **Definition:** `frozenset()` creates an immutable variant of a set[cite: 1].
- *Example:* Because it cannot be altered after creation, a frozen set is hashable and can be used as a dictionary key[cite: 1].