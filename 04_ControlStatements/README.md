**Module 4: Control Statements - Core Concepts**[cite: 1]

**1. Principles of Control Flow**
* By default, Python executes scripts sequentially[cite: 1]. Control statements introduce decision trees that selectively run code blocks based on `True` or `False` evaluations[cite: 1].
* Python strictly enforces indentation (typically 4 spaces) to demarcate code blocks instead of using braces `{}`[cite: 1].
* **Truthiness:** Non-zero numbers, populated sequences, and text evaluate to `True`. Zero, `None`, and empty collections (`""`, `[]`) evaluate to `False`[cite: 1].

**2. Conditional Structures**
* **`if` Statement:** Evaluates a single condition. If `True`, the indented block runs; if `False`, it is skipped[cite: 1].
* **`if-else` Statement:** A dual-branch mechanism where exactly one block is guaranteed to execute[cite: 1].
* **`if-elif-else` Ladder:** Evaluates mutually exclusive conditions sequentially. The first `True` condition triggers its block, and Python immediately exits the ladder, bypassing the rest[cite: 1, 2].

**3. Advanced Branching**
* **Nested `if` Statements:** Placing an `if` block inside another `if` block. Used for multi-stage validation where secondary checks depend on primary conditions passing[cite: 1].
* **Ternary Operator:** A concise, single-line conditional syntax used for simple assignments (e.g., `value_if_true if condition else value_if_false`)[cite: 1].