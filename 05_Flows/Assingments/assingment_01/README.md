# Assignment 1: Mechanics of Iteration — Loop Architectures & Flow Control

## Overview
This assignment focuses on the core mechanics of definite and conditional iteration. We are building practical scripts to traverse basic data structures, apply loop control statements, and construct multi-dimensional geometric patterns using nested loops.

## Core Terms & Concepts
* **Definite Iteration (`for`):** Iterating sequentially through specific elements of iterables such as numeric ranges, strings, and dictionary mappings.
* **Conditional Iteration (`while`):** Continuously executing a loop block based on a sentinel guard condition.
* **Range Function (`range()`):** Generating arithmetic step sequences (e.g., `range(start, stop, step)`).
* **Loop Control Statements:**
  * `continue`: Halts the current cycle and skips to the next iteration.
  * `break`: Immediately terminates the loop entirely.
  * `else` (Loop Clause): An optional block that triggers only if the loop reaches natural completion without being interrupted by a `break`.
* **Nested Loops:** Running an inner loop entirely for every single cycle of an outer loop, heavily used for matrix and pattern generation.

## Task Breakdown
**Task 1: Definite Traversal Across Data Structures (`task1_loop_traversal.py`)**
Demonstrates `for` loop mechanics across three distinct structures. The script generates an arithmetic sequence using `range()` to accumulate a running sum, iterates through a string token while skipping hyphens using `continue`, and unpacks a dictionary to display server nodes and their statuses.

**Task 2: Conditional Guards, Loop `else` & Star Matrix Synthesis (`task2_while_and_patterns.py`)**
Demonstrates conditional flow and nested architecture. The script runs a `while` countdown that triggers a natural `else` completion, runs an infinite `while True` listener that halts prematurely via `break` (bypassing the `else` clause entirely), and utilizes nested `for` loops to synthesize a centered star pyramid based on user input.