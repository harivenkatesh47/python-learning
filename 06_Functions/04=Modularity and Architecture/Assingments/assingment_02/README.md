# Assignment 2: Applied System Architecture — The Enterprise Banking Engine

## Overview
This assignment synthesizes core procedural programming, data structures, conditional control flows, defensive validations, and modular design patterns into a complete banking CLI application.

## Learning Objectives
* Structure a multi-tier console application with strict separation between persistent state storage and business logic mutation functions.
* Implement defensive financial guards (overdraft prevention, non-positive entry rejection, format handling).
* Maintain an append-only audit trail ledger across transaction sessions.
* Ensure clear startup execution using `if __name__ == "__main__":`.

## Task Breakdown
**Task 1: Banking Business Logic Module (`banking_core.py`)**
Build an independent, UI-agnostic banking engine managing ledger accounts. Functions include `initialize_account`, `get_balance`, `process_deposit`, and `process_withdrawal`. Implement input validation rejecting zero or negative amounts, enforce overdraft protection blocking withdrawals exceeding the current balance, and maintain a timestamped/string transaction history ledger. Embed an internal automated self-test suite guarded by `if __name__ == "__main__":`.

**Task 2: Banking CLI Interactive Driver (`task_banking_driver.py`)**
Build an interactive console driver that imports `banking_core.py`. Manage the user session via a persistent `while True` loop presenting options for balance inquiry, deposit processing, withdrawal execution, and session termination. Wrap numeric prompts in defensive `try-except ValueError` blocks to reject invalid strings, pass sanitized inputs into core functions, and print formatted receipts based on returned status flags.