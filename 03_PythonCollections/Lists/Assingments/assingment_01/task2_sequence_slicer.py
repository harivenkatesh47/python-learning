"""
Task 2: Sequence Slicing & Sequence Concatenation Pipeline
Module: Module 05 - Lists in Python
"""

def main():
    print("=== Telemetry Signal Pipeline ===")
    
    # 1 & 2. Baseline calibration and repetition
    calibration_pulse = [0.0, 0.5]
    baseline_sequence = calibration_pulse * 3
    
    # 3. Continuous telemetry stream
    telemetry_stream = [12.4, 15.8, 18.2, 22.1, 25.0, 27.4, 31.2, 35.6]
    
    # 4. Slicing operations
    first_quartile = telemetry_stream[:3]
    trailing_window = telemetry_stream[-3:]
    subsampled_stream = telemetry_stream[::2]
    
    # 5. Concatenation
    combined_stream = baseline_sequence + subsampled_stream
    
    # 6. Threshold flag check
    is_anomaly_free = 99.9 not in combined_stream
    
    # 7. Formatted outputs
    print(f"Repeated Baseline Calibration : {baseline_sequence}")
    print(f"First Quartile (Start:3)      : {first_quartile}")
    print(f"Trailing Window (-3:)         : {trailing_window}")
    print(f"Subsampled Stream (::2)       : {subsampled_stream}")
    print(f"Combined Session Stream       : {combined_stream}")
    print(f"Threshold Anomaly (99.9) Free : {is_anomaly_free}")
    print(f"Total Sensor Data Points      : {len(combined_stream)}")

if __name__ == "__main__":
    main()