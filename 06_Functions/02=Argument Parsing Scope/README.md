# Module 09 (Part 2): Argument Parsing & Scope - Core Notes

## 1. Function Parameter Types & Precedence
* **Positional Arguments:** Values bound to parameters strictly in sequence from left to right based on their position in the call signature.
* **Keyword Arguments:** Values explicitly mapped to parameter names during invocation (`param=value`), allowing arguments to arrive in any arbitrary order.
* **Default Arguments:** Parameters assigned fallback values in the signature (`def func(x, y=10):`). If the caller omits that parameter, the default is applied.
* **Signature Ordering Rules:** Positional parameters must strictly precede default arguments in the function definition (e.g., `def func(a, b=5)` is valid; `def func(a=5, b)` raises a `SyntaxError`).

## 2. Variable-Length Arguments (`*args` and `**kwargs`)
* **`*args` (Arbitrary Positional Arguments):** Prefixed with a single asterisk. Gathers any arbitrary number of extra positional arguments into an immutable `tuple`.
* **`**kwargs` (Arbitrary Keyword Arguments):** Prefixed with a double asterisk. Ingests any arbitrary number of named keyword arguments into a standard `dict`.
* **Standard Signature Precedence:** When combining argument forms in a single function, the signature must follow this strict ordering:
  `def function_name(positional_args, *args, default_args=val, **kwargs):`

## 3. Variable Scope & Lifetime
* **Local Scope:** Variables created within a function body. They exist only for the duration of the function execution and are destroyed upon returning.
* **Global Scope:** Variables defined at the root module level. They are readable across all functions in the script.
* **Variable Shadowing:** Declaring a variable inside a function with the exact same identifier as a global variable temporarily masks the global reference within that local execution frame.
* **The `global` Keyword:** Used inside a local function to explicitly declare intent to modify or reassign a module-level variable (`global var_name`). Without this keyword, reassigning creates a new local variable instead.
* **Mutability vs. Reassignment:** Modifying a global mutable structure (e.g., calling `.append()` on a globally scoped list or adding keys to a dictionary) works without the `global` keyword; however, rebinding or reassigning the variable reference itself strictly requires `global`.