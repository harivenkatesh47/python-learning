**Dictionaries - Core Concepts**

**1. Introduction to Dictionaries**
* Dictionaries are mutable mappings of unique, hashable keys to specific values, enclosed in curly braces `{key: value}`[cite: 1].
* Keys must be immutable (like strings, numbers, or tuples); mutable types like lists or standard dictionaries cannot be keys[cite: 1].

**2. CRUD Operations (Create, Read, Update, Delete)**
* **Insertion/Update:** Assign values directly via `d[key] = value` or in bulk using `d.update({key: value})`[cite: 1].
* **Safe Extraction:** Use `.get(key, fallback)` to fetch values safely without triggering a `KeyError` on missing keys[cite: 1].
* **Deletion:** Use `del d[key]` to delete directly, or `d.pop(key)` to remove a pair and return its value[cite: 1].

**3. Dictionary Views**
* `.keys()` returns a dynamic view of all dictionary keys[cite: 1].
* `.values()` returns a dynamic view of all values[cite: 1].
* `.items()` returns key-value pairs as `(key, value)` tuples, standard for loop iteration[cite: 1].

**4. Memory Mechanics (Copying)**
* **Direct Assignment (`b = a`):** Creates a memory alias; mutating `b` mutates `a`[cite: 1].
* **Shallow Copy (`.copy()`):** Duplicates the top-level container, but nested mutable objects still reference the original memory addresses[cite: 1]. Modifying a nested list in the copy mutates the original[cite: 1].
* **Deep Copy (`copy.deepcopy()`):** Recursively clones the entire object graph, constructing fully independent copies of nested structures to prevent side-effect mutations[cite: 1].