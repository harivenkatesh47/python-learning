# Assignment 1: Mechanics of Iteration — Loop Architectures & Flow Control

## Overview
This assignment focuses on the core mechanics of definite and conditional iteration[cite: 1]. We are building practical scripts to traverse basic data structures, apply loop control statements, and construct multi-dimensional geometric patterns using nested loops[cite: 1].

## Core Terms & Concepts
* **Definite Iteration (`for`):** Iterating sequentially through specific elements of iterables such as numeric ranges, strings, and dictionary mappings[cite: 1].
* **Conditional Iteration (`while`):** Continuously executing a loop block based on a sentinel guard condition[cite: 1].
* **Range Function (`range()`):** Generating arithmetic step sequences (e.g., `range(start, stop, step)`)[cite: 1].
* **Loop Control Statements:**
  * `continue`: Halts the current cycle and skips to the next iteration[cite: 1].
  * `break`: Immediately terminates the loop entirely[cite: 1].
  * `else` (Loop Clause): An optional block that triggers only if the loop reaches natural completion without being interrupted by a `break`[cite: 1].
* **Nested Loops:** Running an inner loop entirely for every single cycle of an outer loop, heavily used for matrix and pattern generation[cite: 1].

## Task Breakdown
**Task 1: Definite Traversal Across Data Structures (`task1_loop_traversal.py`)**
Demonstrates `for` loop mechanics across three distinct structures. The script generates an arithmetic sequence using `range()` to accumulate a running sum, iterates through a string token while skipping hyphens using `continue`, and unpacks a dictionary to display server nodes and their statuses[cite: 1].

**Task 2: Conditional Guards, Loop `else` & Star Matrix Synthesis (`task2_while_and_patterns.py`)**
Demonstrates conditional flow and nested architecture. The script runs a `while` countdown that triggers a natural `else` completion, runs an infinite `while True` listener that halts prematurely via `break` (bypassing the `else` clause entirely), and utilizes nested `for` loops to synthesize a centered star pyramid based on user input[cite: 1].