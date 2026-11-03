# Assignment 2: Sets - Set Algebra & Frozen Sets

## Overview
This assignment focuses on advanced mathematical set operations and immutable set architecture. We are building a network vulnerability scanner and a security policy engine to map system privileges.

## Core Terms & Concepts Explained
* **Union (`|`):** Merges elements from two sets, keeping all unique items.
* **Intersection (`&`):** Extracts only the elements present in both sets simultaneously.
* **Difference (`-`):** Extracts elements that exist in the primary set but are entirely absent from the secondary set.
* **Symmetric Difference (`^`):** Extracts non-overlapping elements that exist in only one of the sets.
* **Frozen Sets (`frozenset`):** An immutable version of a set. It cannot be altered after creation, making it hashable and eligible to be used as a dictionary key.

## Task Breakdown
**Task 1: Security Network Vulnerability Scanner**
We cross-reference two CVE threat profiles. The script uses set algebra to identify the total combined threat surface (`|`), confirmed overlaps (`&`), and exclusive discrepancies (`-` and `^`) between the scanners.

**Task 2: Frozen Set Security Policy Engine**
We establish immutable security roles using `frozenset()`. We test the frozen state by trapping an `.add()` attempt, calculate elevated privileges via set difference, and use the frozen set directly as a hashable dictionary key.