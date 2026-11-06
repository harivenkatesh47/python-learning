# 1. Define statistical reduction function returning an unpacked tuple
def analyze_signal_batch(readings):
    """
    Calculates aggregate statistical metrics for a batch of sensor readings.
    
    Parameters:
        readings (list): A list of float telemetry frequencies.
        
    Returns:
        tuple: (total_volume, minimum_frequency, maximum_frequency, arithmetic_mean)
    """
    total = sum(readings)
    min_val = min(readings)
    max_val = max(readings)
    mean_val = round(total / len(readings), 2)
    
    return total, min_val, max_val, mean_val


# 2. Define a helper function to construct a report string
def format_signal_report(station_name, total, min_val, max_val, mean_val):
    """
    Constructs a formatted multiline report from unpacked sensor metrics.
    """
    report = (
        f"--- Signal Processing Report ---\n"
        f"Monitoring Station : {station_name}\n"
        f"Total Data Volume  : {total:.2f} MHz\n"
        f"Minimum Threshold  : {min_val:.2f} MHz\n"
        f"Peak Reading       : {max_val:.2f} MHz\n"
        f"Mean Frequency     : {mean_val:.2f} MHz"
    )
    return report


# 3 & 4 & 5. Execution body establishing a computational pipeline
def main():
    print("=== Telemetry Signal Batch Analyzer ===\n")
    
    sensor_sample = [102.4, 98.7, 110.1, 105.3, 94.6, 108.8]
    
    # Pipeline Step 1: Analyze and unpack directly
    sig_total, sig_min, sig_max, sig_mean = analyze_signal_batch(sensor_sample)
    
    # Pipeline Step 2: Feed unpacked metrics into the formatter
    final_report = format_signal_report("Station-Alpha-9", sig_total, sig_min, sig_max, sig_mean)
    
    print(final_report)


if __name__ == "__main__":
    main()