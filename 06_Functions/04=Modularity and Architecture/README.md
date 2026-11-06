# Functions (Part 4): Modularity, Architecture & Applied Project - Core Notes

## 1. Python Modules & Namespace Isolation
* **Definition of a Module:** Any Python source file (`.py`) containing variable definitions, function declarations, and executable logic.
* **Namespace Isolation:** Modules establish distinct encapsulation boundaries, preventing identifier collisions across independent files.
* **Import Syntaxes:**
  * `import module_name`: Imports the entire module; functions are invoked via dot notation (`module_name.func()`).
  * `from module_name import item`: Pulls a specific function or variable directly into the current namespace.
  * `import module_name as alias`: Aliases the module identifier to provide a concise, readable shorthand.

## 2. Execution State Mechanics: `__name__` and `if __name__ == "__main__":`
* **Built-in Module Variable:** Every Python module maintains an internal string variable named `__name__`.
* **Direct Execution:** When a script is executed directly from the terminal, Python automatically binds `__name__` to `"__main__"`.
* **Imported Execution:** When a script is imported by another module, Python binds `__name__` to the module's actual filename (without the `.py` extension).
* **Entry-Point Guarding:** Placing test suites, CLI runners, or demonstration code inside `if __name__ == "__main__":` guarantees they execute only when run directly, remaining dormant when imported into external drivers.

## 3. Architecture of Multi-Tier Applications
* **Separation of Concerns:** Business logic (state calculation, validation rules) must be segregated cleanly from the user interface (CLI, print statements, user inputs).
* **State Management:** Core logic receives state dictionaries and mutation inputs, validates conditions defensively (e.g., overdraft barriers, positive value enforcement), and returns status flags or updated references.
* **Presentation Layer:** The driver layer handles menu loops, user prompts, error trapping (`try-except`), and displays status messages returned by the business logic functions.