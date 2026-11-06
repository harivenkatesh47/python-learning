# Assignment 1: Custom Modules, Namespace Encapsulation & Entry-Point Guards

## Overview
This assignment demonstrates multi-file project architecture by separating reusable conversion logic from executable driver interfaces, alongside standard library environment diagnostics.

## Learning Objectives
* Build multi-file Python systems by decoupling business functions from interactive CLI drivers.
* Apply import variations (`import`, `from ... import`, `as alias`) cleanly.
* Prevent identifier collisions using module namespace encapsulation.
* Implement `if __name__ == "__main__":` guards to ensure test suites remain dormant during external imports.

## Task Breakdown
**Task 1: Reusable Industrial Unit Converter Module (`converter_utils.py` & `task1_modular_converter.py`)**
Construct a custom utility module (`converter_utils.py`) defining conversion functions for temperature (Celsius to Fahrenheit), distance (Kilometers to Miles), and weight (Kilograms to Pounds). Guard an internal unit-test block using `if __name__ == "__main__":`. Build an external driver script (`task1_modular_converter.py`) that imports the module, gathers user inputs, and displays converted engineering values without triggering the utility script's dormant tests.

**Task 2: Standard Library Math & System Inspector (`task2_stdlib_inspector.py`)**
Access built-in runtime diagnostics and mathematical algorithms via Python standard library modules (`math`, `sys`, and `platform`). Implement a hypotenuse and base-10 logarithm calculator using math functions, inspect the operating system platform and Python interpreter engine version, and encapsulate execution under an entry-point guard.
