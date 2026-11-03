# Assignment 1: Sequential Mutations, Search & Inventory Management

## Overview
This assignment focuses on managing dynamic collections of data using Python lists. We are building two practical scripts: a warehouse queue manager for an e-commerce hub to handle order dispatching, and a telemetry signal pipeline to process and sample raw sensor data. 

## Core Terms & Concepts
* **List Initialization:** Creating a new, empty list container `[]` to hold sequence data.
* **List Mutations:** Altering a list in place without generating a new object in memory.
  * `.append(item)`: Adds a single item to the absolute end of the list.
  * `.insert(index, item)`: Places an item at a specific position, shifting existing items to the right.
  * `.extend(iterable)`: Takes a batch of items (like another list) and adds them individually to the end.
* **Extraction & Deletion:**
  * `.pop(index)`: Removes and returns the item at the targeted position (e.g., `pop(0)` removes the first item).
  * `.remove(value)`: Searches for a specific value and deletes its first occurrence.
* **Membership & Frequency:**
  * `in` / `not in`: Boolean operators to check if a specific item exists inside the list.
  * `.count(value)`: Returns the total number of times an exact value appears.
* **Sequence Slicing & Merging:** 
  * Extracting sub-sections using `list[start:stop:step]`.
  * Using `+` to concatenate two lists and `*` to repeat list elements.

## Task Breakdown
**Task 1: Warehouse Inventory Dispatcher (`task1_inventory_dispatcher.py`)**
We simulate an e-commerce dispatch queue. The script initializes an active order list, inserts a rush priority order at the front (index 0), appends standard orders, and extends the queue with a batch of returns. It searches the queue for a specific order to cancel using `.remove()`, and processes the first and last orders using `.pop()`.

**Task 2: Sequence Slicing & Concatenation Pipeline (`task2_sequence_slicer.py`)**
We process an incoming stream of sensor data. The script creates a baseline calibration list using the repetition operator (`*`), then extracts specific data windows using positive slicing, negative trailing slicing, and step slicing (`[::2]`). It merges the calibration sequence with the sampled data using list concatenation (`+`) and checks for anomalies using the `not in` operator.