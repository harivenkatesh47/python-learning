# Assignment 1: Recursion Dynamics & First-Class Higher-Order Handlers

## Overview
This assignment explores functional programming paradigms in Python, focusing on recursive call-stack mechanics and higher-order function architectures. You will construct a recursive hierarchical file system inspector to compute nested storage and directory depth, followed by an extensible payment processing pipeline that treats functions as first-class citizens.

## Learning Objectives
* Construct recursive algorithms with terminating base cases and reductive recursive steps.
* Manage call-stack execution safely and avoid infinite recursion traps.
* Treat functions as first-class citizens by passing them as operational callbacks to higher-order functions.
* Dispatch business logic dynamically through strategy registries without relying on repetitive conditional ladders.

## Task Breakdown
**Task 1: Recursive File System Directory Size & Depth Tracker (`task1_recursive_inspector.py`)**
Traverse a nested hierarchical directory tree represented using nested dictionaries and child lists. Implement `calculate_total_storage(node)` to recursively aggregate total file storage in kilobytes, and `calculate_max_depth(node)` to determine the deepest folder nesting level. Verify clean call-stack unwinding upon reaching terminal subdirectories containing no child elements.

**Task 2: Higher-Order Payment Gateway & Fee Calculator (`task2_higher_order_gateway.py`)**
Build an extensible financial transaction gateway. Define discrete fee calculation strategy routines (`standard_fee`, `international_fee`, and `premium_client_fee`). Implement a higher-order engine `process_payment(transaction_id, amount, fee_strategy_func)` that accepts a fee strategy callback function directly, evaluates the charge, and returns a structured record with computed fee breakdowns. Query the functions dynamically from a strategy registry mapping.

