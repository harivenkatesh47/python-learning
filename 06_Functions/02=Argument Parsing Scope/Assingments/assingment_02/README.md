# Assignment 2: Variable Scope, Shadowing & Mutability Guards

## Overview
This assignment examines execution namespaces and the boundaries of variable scope in Python. You will construct a global audit counter demonstrating the mechanics of local variable shadowing and the `global` keyword, followed by a shared cache manager exploring in-place mutations versus variable reassignments.

## Learning Objectives
* Distinguish between local scope and global scope variables.
* Demonstrate variable shadowing where local identifiers temporarily mask global names.
* Apply the `global` keyword to deliberately modify module-level state from within a local function.
* Contrast reassigning global variables versus mutating mutable objects (like lists or dictionaries) in place.

## Task Breakdown
**Task 1: Audit Log State Counter & Shadowing Demonstration (`task1_scope_auditor.py`)**
Track global transaction counts while illustrating the distinction between local shadowing and explicit global state updates. Establish root-level global variables (`system_status` and `transaction_count`), demonstrate local shadowing inside a function without mutating module state, use the `global` keyword to increment transaction totals and alter operational modes, and implement a reset routine to restore default state.

**Task 2: Shared Cache Mutation vs Reassignment (`task2_cache_manager.py`)**
Examine how mutable data structures in the global scope can be updated in-place without the `global` keyword, compared to reassigning variable references which strictly requires `global`. Implement routines that append records to a globally referenced list or dictionary directly, contrast this with an attempt to rebind or reassign the global reference, and evaluate the resulting namespace states.