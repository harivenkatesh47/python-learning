**Sets & Frozen Sets - Core Concepts**

**1. Introduction to Sets**
* Sets are unordered, unindexed collections of unique, hashable elements enclosed in curly braces `{}`[cite: 1].
* Converting a sequence to a set automatically deduplicates repeating entries[cite: 1].
* They do not guarantee insertion order and do not support index slicing[cite: 1].

**2. Set Mutations**
* `.add(item)` inserts a single element[cite: 1].
* `.remove(item)` deletes an element but raises a `KeyError` if absent[cite: 1].
* `.discard(item)` deletes an element safely, failing silently if it does not exist[cite: 1].

**3. Mathematical Set Algebra**
* **Union (`|`):** Merges all unique elements from both sets[cite: 1].
* **Intersection (`&`):** Retains only elements present in both sets simultaneously[cite: 1].
* **Difference (`-`):** Retains elements present in the primary set but entirely absent from the secondary set[cite: 1].
* **Symmetric Difference (`^`):** Retains elements in either set, but not in both[cite: 1].

**4. Frozen Sets**
* `frozenset()` creates an immutable variant of a set[cite: 1].
* Because it cannot be altered after creation, it is hashable and can be used as a dictionary key or as an element within another set[cite: 1].