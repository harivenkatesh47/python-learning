# Module 05: Loops - Revision Notes

## 1. Core Principles of Iteration
- **Iteration Mechanics:** Loops automate repetitive code execution over sequential data or condition-driven intervals.
- **Iterables:** Any object capable of returning its members one at a time (e.g., lists, strings, dictionaries, `range()`).

## 2. Definite & Conditional Iteration
- **`for` Loop:** Iterates sequentially through each element of an iterable until the collection is exhausted.
- **`while` Loop:** Continuously evaluates a boolean conditional statement before running each cycle, repeating until the condition becomes `False`.
- **`range()` Function:** Generates immutable sequences of arithmetic progressions via `range(start, stop, step)`.

## 3. Loop Control Statements
- **`break`:** Terminates the loop immediately, jumping execution to the first statement outside the loop block.
- **`continue`:** Halts the current cycle immediately, skipping remaining instructions and advancing to the next iteration.
- **`else` Clause:** Runs only if the loop terminates normally (exhausting the iterable or when the `while` condition becomes `False`); bypassed if terminated via `break`.

## 4. Applied Mechanics
- **Nested Loops:** A loop contained within another loop, commonly used for 2D grids and matrices.
- **Random Module:** `random.randint(a, b)` generates pseudo-random integers within a bounded interval, useful in while-loop simulations.