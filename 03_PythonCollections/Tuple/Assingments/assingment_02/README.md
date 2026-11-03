# Assignment 2: Tuples - Record Transformation & Multi-Dimensional Data

## Overview
This assignment scales up to complex tuple structures. We are building an academic roster ledger and a financial transaction audit history to practice multi-level data extraction and mathematical aggregations.

## Core Terms & Concepts Explained
* **Nested Tuples:** Tuples contained within other tuples, used for structuring tabular or multi-dimensional records.
* **Multi-Dimensional Indexing:** Accessing nested elements using chained brackets, such as `roster[row][col]`.
* **Numeric Aggregations:** Using built-in functions like `sum()`, `min()`, and `max()` over numeric tuples.
* **Type Casting (Mutability Hack):** Temporarily converting an immutable tuple into a mutable `list()` to apply updates, then casting it back to a `tuple()`.

## Task Breakdown
**Task 1: Academic Roster Ledger**
We parse a nested tuple of student grades. The script accesses specific exam scores using multi-index notation, calculates performance metrics, and corrects a grading error by temporarily casting a tuple to a list and back.

**Task 2: Transaction Audit History**
We process a ledger of deposits and withdrawals. The script calculates financial extremes and total volume, confirms that `.append()` fails on tuples, and creates an updated ledger sequence via tuple concatenation.