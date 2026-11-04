# Assignment 2: Real-World Systems — Applied Problem Solving

## Overview
This assignment applies looping structures to solve practical, real-world problems. We are building a retail financial ledger, an automated warehouse restocker, and a state-driven diagnostic simulation[cite: 1, 4].

## Core Terms & Concepts
* **Manual Aggregations:** Calculating running totals, maximums, and minimums systematically using loop counters and condition checks instead of built-in math functions[cite: 1, 4].
* **Dynamic Filtering:** Sifting through collections inside a loop to sort or mutate data dynamically based on thresholds[cite: 1, 4].
* **State-Driven Simulations:** Using the `random` module (`random.randint()`) to generate pseudo-random integers for interactive logic[cite: 1, 4].
* **Persistent Prompts:** Using a `while True` loop combined with defensive `try-except ValueError` blocks to safely demand user input until valid data or a specific exit condition is met[cite: 1, 4].

## Task Breakdown
**Task 1: Retail Store Day-End Ledger & Extremes Tracker (`task1_ledger_extremes.py`)**
Processes a batch of cash-register receipts. The script manually iterates through the data to accumulate gross revenue, identifies the peak and lowest ticket sales using tracking variables, and filters the transactions into high-tier and standard categories[cite: 4].

**Task 2: Warehouse Low-Stock Restocking Engine (`task2_inventory_restocker.py`)**
Manages a dictionary-based warehouse inventory. The script loops through all product keys and values, checks them against a critical low-stock threshold, and dynamically mutates the dictionary in-place to restock depleted items[cite: 4].

**Task 3: Interactive Diagnostic Number Guessing Simulation (`task3_diagnostic_guessing.py`)**
Constructs an interactive CLI game. The system generates a hidden target number using `random.randint()` and employs a continuous `while True` loop to solicit user guesses. It provides high/low routing hints, traps invalid string inputs using `try-except`, and terminates the loop via `break` when the user successfully guesses the number[cite: 4].