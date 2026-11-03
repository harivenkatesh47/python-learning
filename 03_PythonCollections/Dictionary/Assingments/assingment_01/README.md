# Assignment 1: Dictionaries - Key-Value CRUD & Lookups

## Overview
This assignment introduces dictionary mapping structures. We are building a server fleet hardware registry and an inventory price evaluator to manage dynamic key-value data dynamically.

## Core Terms & Concepts Explained
* **Dictionaries:** Mutable data structures mapping unique, hashable keys to specific values, formatted as `{key: value}`.
* **Create & Update:** Assigning values via `dict[key] = value` or merging multiple pairs at once using `.update()`.
* **Safe Extraction:** Using `.get(key, fallback)` to fetch values without triggering a `KeyError` if the key is missing.
* **Deletion:** Using `.pop(key)` to remove a pair and return its value, or `del dict[key]` to delete it directly.
* **Dictionary Views:** Extracting live structural data using `.keys()`, `.values()`, and `.items()` (which yields key-value tuples).

## Task Breakdown
**Task 1: Server Fleet Hardware Registry**
We manage active host configurations. The script updates specifications dynamically, decommissions fields using `.pop()` and `del`, queries missing keys safely via `.get()`, and prints the registry using `.items()`.

**Task 2: Inventory Price & Stock Evaluator**
We map SKU names to stock units and pricing. We calculate the total units in the warehouse using `sum()` on `.values()` and cross-reference multiple dictionaries to compute total asset valuation for specific items.