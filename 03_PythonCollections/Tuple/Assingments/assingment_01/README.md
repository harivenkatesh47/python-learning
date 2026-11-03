# Assignment 1: Tuples - Immutability, Indexing & Unpacking

## Overview
This assignment covers the foundations of fixed, unchangeable data collections using Python tuples. We are building a GPS route waypoint ledger and an immutable sensor calibration packet to enforce strict data integrity.

## Core Terms & Concepts Explained
* **Tuples:** Ordered, immutable collections enclosed in parentheses `()`. Elements cannot be reassigned or deleted once the tuple is created.
* **Tuple Unpacking:** Extracting items from a tuple into distinct variables (e.g., `lat, lon = coordinates`).
* **Single-Element Tuples:** Tuples with just one item, requiring a trailing comma `(item,)` so Python recognises them as tuples.
* **Sequence Operations:** Using concatenation `+` to merge tuples, repetition `*` to duplicate them, and index slicing `[start:stop:step]` to extract specific data windows.

## Task Breakdown
**Task 1: GPS Route Waypoint Ledger**
We process fixed geographic coordinates for a logistics route. The script slices out specific waypoints, counts loop occurrences using `.count()`, and explicitly demonstrates tuple immutability by intentionally failing a coordinate mutation attempt.

**Task 2: Immutable Sensor Calibration Packet**
We generate a hardware configuration packet. The script duplicates baseline tolerance signals using the repetition operator `*`, merges them with device metadata using `+`, and verifies threshold safety using `in` and `not in`.