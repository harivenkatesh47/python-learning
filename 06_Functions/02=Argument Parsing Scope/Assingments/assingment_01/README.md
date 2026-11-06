# Assignment 1: Argument Signatures & Dynamic Parameter Ingestion

## Overview
This assignment explores parameter binding, argument precedence, and dynamic variable-length ingestion using `*args` and `**kwargs`. You will build an enterprise microservice endpoint configurator and a multi-sensor telemetry aggregator that handle mandatory positional inputs, default parameters, and arbitrary metadata.

## Learning Objectives
* Define and invoke functions using positional, keyword, and default parameters.
* Enforce signature ordering: positional arguments must strictly precede default parameters.
* Collect arbitrary positional arguments using `*args` as an immutable tuple.
* Ingest variable keyword attributes using `**kwargs` as a dictionary.

## Task Breakdown
**Task 1: Enterprise Microservice Endpoint Configurator (`task1_endpoint_configurator.py`)**
Construct API endpoint connection URIs supporting positional host inputs, optional default configurations, and arbitrary URL query parameters using `**kwargs`. Define `configure_endpoint(service_name, host, port=8080, protocol="https", **query_params)` with a docstring, format the base URI, dynamically append query strings from `query_params.items()`, and invoke the function using positional arguments, explicit overrides, and dynamic keyword parameters.

**Task 2: Multi-Sensor Telemetry Aggregator (*args & **kwargs) (`task2_telemetry_aggregator.py`)**
Process a variable number of numerical sensor data points using `*args` and attach arbitrary contextual metadata using `**kwargs`. Define `aggregate_telemetry(sensor_id, *readings, unit="Celsius", **metadata)` adhering to strict signature precedence, validate that incoming readings are non-empty, compute statistical reductions (`len()`, `min()`, `max()`, and mean), and return a structured dictionary containing the metrics and unpacked metadata.