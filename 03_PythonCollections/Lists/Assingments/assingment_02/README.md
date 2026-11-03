# Assignment 2: Numerical Aggregations, In-Place Ordering & Nested Matrices

## Overview
This assignment advances into data analytics and multi-dimensional grid structures. We are building two scripts: a grade analytics engine that calculates class statistics from a list of scores, and an environmental sensor grid transformer that maps and mutates 2D spatial data.

## Core Terms & Concepts
* **Numerical Aggregations:** Built-in Python functions that perform math over an entire sequence of numbers.
  * `sum(list)`: Adds all numbers in the list together.
  * `min(list)` / `max(list)`: Finds the lowest and highest values in the sequence.
  * `len(list)`: Counts the total number of elements present.
* **In-Place Ordering:** Sorting list elements logically without allocating a new list in memory.
  * `.sort()`: Arranges numeric or alphabetical data in ascending order.
  * `.sort(reverse=True)`: Arranges data in descending order.
  * `.reverse()`: Inverts the current sequence of the list entirely backwards.
* **Nested Lists (2D Matrices):** Lists that contain other lists inside them, commonly used to represent grids, tables, or spatial matrices.
* **Multi-Index Bracket Notation:** Accessing data inside a nested list using chained brackets, such as `matrix[row][col]`. 

## Task Breakdown
**Task 1: Student Exam Score Analytics Engine (`task1_score_analytics.py`)**
We analyze a batch of raw student exam scores. The script calculates the class mean using `sum()` divided by `len()`, and identifies the lowest and highest performers using `min()` and `max()`. It then counts how many students achieved the peak score and organizes the final dataset into ascending, descending, and inverted ranks using in-place ordering methods.

**Task 2: 2D Sensor Grid Matrix Transformer (`task2_grid_transformer.py`)**
We map a 3x3 environmental sensor grid. The script models three distinct temperature zones using nested lists. We navigate to a specific core reading using `[row][col]` indexing to correct an anomalous temperature spike by mutating it in place. We then calculate row-level metrics (the mean and peak of specific sub-lists) and expand the matrix architecture by appending new readings to an existing zone and dynamically adding an entirely new 4th zone to the master grid.