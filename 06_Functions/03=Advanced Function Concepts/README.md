# Functions(Part 3): Advanced Function Concepts - Core Notes

## 1. Recursive Functions
* **Principles of Recursion:** A technique where a function calls itself directly or indirectly to solve a problem by decomposing it into smaller, identical sub-problems.
* **Base Case:** The mandatory terminating condition that returns a concrete value without making additional recursive calls.
* **Recursive Step:** The logic that modifies the state and invokes the function recursively, driving inputs progressively closer to the base case.
* **Call Stack Mechanics:** Each recursive invocation pushes a frame onto the call stack. Exceeding Python's recursion limit (~1000 frames) triggers a `RecursionError: maximum recursion depth exceeded`.

## 2. First-Class Functions & Higher-Order Functions
* **First-Class Citizens:** In Python, functions are treated as standard objects. They can be assigned to variables, stored in data structures (lists, dictionaries), passed as arguments to other functions, and returned from functions.
* **Higher-Order Functions:** Functions that accept another function as an operational callback or return a function as their result.

## 3. Lambda Functions (Anonymous Functions)
* **Syntax:** Defined using the `lambda` keyword: `lambda arguments: expression`.
* **Single-Expression Limit:** Limited to evaluating a single line expression; statements and multi-line loops cannot be placed inside a lambda.
* **Implicit Return:** Automatically returns the evaluated result of the single expression without writing an explicit `return` keyword.

## 4. Functional Transformations: `map()` and `filter()`
* **`map(function, iterable)`:** Applies the function to every item in the iterable, returning a lazy map iterator of transformed results. Cast to `list()` or `tuple()` to evaluate.
* **`filter(function, iterable)`:** Evaluates every item against a boolean predicate function, returning an iterator yielding only elements where the condition evaluates to `True`.