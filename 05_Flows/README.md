# Module 05: Loops - Revision Notes

## 1. Core Principles of Iteration
- **Iteration Mechanics:** Loops automate repetitive code execution over sequential data or condition-driven intervals[cite: 1].
- **Iterables:** Any object capable of returning its members one at a time (e.g., lists, strings, dictionaries, `range()`)[cite: 1].

## 2. Definite & Conditional Iteration
- **`for` Loop:** Iterates sequentially through each element of an iterable until the collection is exhausted[cite: 1].
- **`while` Loop:** Continuously evaluates a boolean conditional statement before running each cycle, repeating until the condition becomes `False`[cite: 1].
- **`range()` Function:** Generates immutable sequences of arithmetic progressions via `range(start, stop, step)`[cite: 1].

## 3. Loop Control Statements
- **`break`:** Terminates the loop immediately, jumping execution to the first statement outside the loop block[cite: 1].
- **`continue`:** Halts the current cycle immediately, skipping remaining instructions and advancing to the next iteration[cite: 1].
- **`else` Clause:** Runs only if the loop terminates normally (exhausting the iterable or when the `while` condition becomes `False`); bypassed if terminated via `break`[cite: 1].

## 4. Applied Mechanics
- **Nested Loops:** A loop contained within another loop, commonly used for 2D grids and matrices[cite: 1].
- **Random Module:** `random.randint(a, b)` generates pseudo-random integers within a bounded interval, useful in while-loop simulations[cite: 1].