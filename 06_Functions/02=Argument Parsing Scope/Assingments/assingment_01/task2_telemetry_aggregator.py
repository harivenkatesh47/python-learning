def aggregate_telemetry(sensor_id, *readings, unit="Celsius", **metadata):
    if not readings:
        return "Warning: No telemetry readings provided for aggregation."
        
    readings_count = len(readings)
    min_reading = min(readings)
    max_reading = max(readings)
    average_reading = round(sum(readings) / readings_count, 2)
    
    summary = {
        "Sensor ID": sensor_id,
        "Sample Count": f"{readings_count} readings",
        "Min / Max": f"{min_reading:.2f} / {max_reading:.2f} {unit}",
        "Average": f"{average_reading:.2f} {unit}",
        "Metadata": metadata
    }
    
    return summary

def main():
    print("=== Telemetry Aggregator System ===")
    
    print("\n--- Temperature Stream Report ---")
    temp_report = aggregate_telemetry("TEMP-NODE-01", 21.5, 23.0, 22.8, 24.1, 20.9, site="Floor-2", calibrated=True)
    for key, value in temp_report.items():
        print(f"{key:<12} : {value}")
        
    print("\n--- Pressure Stream Report ---")
    pressure_report = aggregate_telemetry("PRESSURE-04", 101.3, 102.1, 100.8, unit="kPa", zone="Sector-B")
    for key, value in pressure_report.items():
        print(f"{key:<12} : {value}")

if __name__ == "__main__":
    main()