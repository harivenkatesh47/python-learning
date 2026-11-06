# Assignment 1: Function Declaration, Execution Lifecycle & Docstring Introspection

## Overview
This assignment, derived from the AI Engineer file, focuses on the core mechanics of user-defined functions[cite: 1]. You will define and invoke reusable functions that adhere to the DRY (Don't Repeat Yourself) design principle[cite: 1]. 

## Learning Objectives
* Define and invoke reusable functions adhering strictly to the DRY principle[cite: 1].
* Distinguish between explicit return values and the implicit `None` fallback[cite: 1].
* Write standardized PEP 257 docstrings within function bodies[cite: 1].
* Inspect documentation dynamically at runtime using `__doc__` and `help()`[cite: 1].

## Task Breakdown
**Task 1: Industrial Workstation Status Reporter (`task1_workstation_reporter.py`)**
Define a procedural function named `log_machine_startup` that logs machine initialization without a return statement, demonstrating Python's default `None` return behavior[cite: 1]. Define a second function, `assess_operating_temperature`, that evaluates core temperature and returns a safety rating ("NORMAL", "ELEVATED", or "CRITICAL")[cite: 1]. Invoke both functions, verify that the procedural function returns `None`, and programmatically print the docstring of the validation function using its `__doc__` attribute[cite: 1].

**Task 2: Geometric Metric Transformer (`task2_geometry_helper.py`)**
Eliminate repetitive arithmetic by wrapping geometric formulas into modular functions[cite: 1]. Create `calculate_circle_area(radius)` and `calculate_rectangle_perimeter(length, width)`, complete with docstrings detailing the inputs and mathematical formulas applied[cite: 1]. Demonstrate the DRY principle by invoking the circle function multiple times with different radii and printing the cleanly formatted results[cite: 1].