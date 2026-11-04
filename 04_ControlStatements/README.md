# Module 04: Control Statements - Revision Notes

## 1. Principles of Control Flow
- **Decision Trees:** Control statements introduce branching that selectively runs code blocks based on `True` or `False` conditional evaluations[cite: 1].
- **Indentation:** Python strictly enforces indentation (typically 4 spaces) to demarcate code blocks instead of using braces `{}`[cite: 1].
- **Truthiness:** Non-zero numbers and populated sequences evaluate to `True`, while zero, `None`, and empty collections evaluate to `False`[cite: 1].

## 2. Conditional Structures
- **`if` Statement:** Evaluates a single condition; if `True`, the indented block executes[cite: 1].
- **`if-else` Statement:** A dual-branch mechanism where exactly one block is guaranteed to execute[cite: 1].
- **`if-elif-else` Ladder:** Evaluates mutually exclusive conditions sequentially; the first `True` condition triggers its block, and execution exits the ladder immediately[cite: 1].

## 3. Advanced Branching
- **Nested `if` Statements:** Placing an `if` block inside another `if` block for multi-stage validation[cite: 1].
- **Ternary Operator:** A concise, single-line conditional syntax designed for simple value assignments[cite: 1].
- *Example:* `value_if_true if condition else value_if_false`[cite: 1].