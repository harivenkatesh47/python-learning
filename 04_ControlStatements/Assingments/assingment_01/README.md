# Assignment 1: Conditional Branching, Threshold Triggers & Priority Routing

## Overview
This assignment focuses on implementing discrete decision pathways using conditional logic. We are building practical applications that rely on evaluating multi-factor conditions, including a server thermal governor for hardware management and a high-volume transaction risk screener for fraud detection.

## Core Terms & Concepts Explained
* **Conditional Branching:** Using `if`, `elif`, and `else` statements to route execution through different logical paths based on whether conditions are `True` or `False`[cite: 1, 2].
* **Relational Operators:** Symbols (`<`, `>`, `<=`, `>=`, `==`, `!=`) used to compare values and establish thresholds[cite: 1, 2].
* **Logical Operators:** Keywords (`and`, `or`, `not`) used to combine multiple relational expressions into a single compound condition[cite: 1, 2].
* **Defensive Input Parsing:** Wrapping user inputs inside a `try-except ValueError` block to gracefully trap and handle non-numeric data without crashing the program[cite: 1, 2].

## Task Breakdown
**Task 1: Server Load & Thermal Governor (`task1_thermal_governor.py`)**
We evaluate real-time server telemetry. The script takes CPU utilization and core temperature as inputs, verifies they are within operational bounds, and uses a multi-tier `if-elif-else` ladder to trigger specific hardware responses, such as emergency throttling, high-performance cooling, or eco mode[cite: 1, 2].

**Task 2: High-Volume Transaction Risk Screener (`task2_risk_screener.py`)**
We assess incoming financial transactions for fraud risk. The script converts "yes"/"no" string inputs into boolean flags and routes transactions into specific review queues based on the transfer amount, international status, and device verification using complex logical checks[cite: 1, 2].