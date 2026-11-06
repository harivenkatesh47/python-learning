# Assignment 2: Multiple Return Values, Tuple Unpacking & Operational Pipelines

## Overview
This assignment explores how inputs are processed and how multiple discrete values are returned and unpacked[cite: 1]. You will build linear computational pipelines where the output of one function feeds directly into another[cite: 1].

## Learning Objectives
* Implement user-defined functions that compute and return multiple discrete values[cite: 1].
* Demonstrate automatic tuple packing on function return and unpack values on invocation[cite: 1].
* Build a linear computational pipeline where the output of one function feeds into another[cite: 1].
* Document multi-return structures within PEP 257 docstrings[cite: 1].

## Task Breakdown
**Task 1: Financial Currency & Denomination Splitter (`task1_currency_splitter.py`)**
Process a raw currency float by extracting whole rupees and fractional paise, returning both simultaneously to demonstrate automatic tuple packing[cite: 1]. Create a second function, `compute_tax_breakdown`, that takes a base amount and tax rate, computes the tax and grand total, and returns all three values[cite: 1]. In the execution body, capture the packed tuple, verify its type, and unpack the values directly into discrete variables for formatted console display[cite: 1].

**Task 2: Multi-Sample Signal Analyzer (`task2_signal_analyzer.py`)**
Accept a list of raw telemetry sensor frequencies and compute the total volume, minimum, maximum, and arithmetic mean inside a single function (`analyze_signal_batch`)[cite: 1]. Return all four metrics simultaneously[cite: 1]. Unpack this 4-element tuple directly into distinct variables, and pass them into a secondary helper function named `format_signal_report` to construct and print a formatted multiline summary report[cite: 1].