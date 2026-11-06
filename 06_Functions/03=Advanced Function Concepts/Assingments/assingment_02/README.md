# Assignment 2: Anonymous Functions, Functional Filtering & Data Transformations

## Overview
This assignment explores compact functional programming paradigms using inline lambda expressions combined with Python's built-in `map()` and `filter()` iterators.

## Learning Objectives
* Express single-expression transformations using anonymous `lambda` functions.
* Transform multi-record collections in batch using `map()` with inline lambdas.
* Extract targeted sub-cohorts using `filter()` with boolean conditions.
* Construct multi-stage data pipelines chaining validation, filtering, and string formatting.

## Task Breakdown
**Task 1: Real-Time E-Commerce Price & GST Pipeline (`task1_price_transformer.py`)**
Processes wholesale catalog records. Uses `lambda` with `map()` to calculate an 18% GST surcharge on base numeric prices, and transforms the list of item dictionaries to include calculated retail pricing fields.

**Task 2: Server Cluster Telemetry Screener (`task2_telemetry_screener.py`)**
Audits cluster health logs. Uses `filter()` with lambdas to isolate online server nodes, extracts active node IDs via `map()`, and flags high-risk hardware anomalies where CPU or memory utilization exceeds safety thresholds.

**Task 3: Functional Data Processing Pipeline (`task3_functional_pipeline.py`)**
Builds a sequential three-stage pipeline for test scores: Stage 1 filters out corrupted out-of-bound values using `filter()`, Stage 2 isolates passing marks, and Stage 3 uses `map()` to assign tiered letter grades and produce an evaluation stream.