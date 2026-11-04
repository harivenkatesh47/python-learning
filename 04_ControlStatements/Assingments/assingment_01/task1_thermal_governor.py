def main():
    print("=== Server Thermal Governor System ===")
    try:
        cpu_load = float(input("Enter CPU Load (%): "))
        core_temp = float(input("Enter Core Temperature (°C): "))

        # Validate operational bounds
        if not (0.0 <= cpu_load <= 100.0) or not (0.0 <= core_temp <= 120.0):
            print("\nError: Telemetry out of valid operational bounds. System halted.")
        else:
            # Multi-tier if-elif-else ladder
            if cpu_load >= 90.0 or core_temp >= 85.0:
                mode = "Emergency Throttling"
                action = "Drop clock speeds and alert admin"
            elif cpu_load >= 75.0 and core_temp >= 70.0:
                mode = "High Performance Cooling"
                action = "Spin aux fans to 100%"
            elif cpu_load >= 50.0 or core_temp >= 55.0:
                mode = "Standard Optimization"
                action = "Maintain dynamic cooling"
            else:
                mode = "Eco Mode (Idle)"
                action = "Reduce fan RPM for silent operation"

            # Formatted output
            print("\n--- Thermal Dispatch Report ---")
            print(f"\tLoad State     : {cpu_load:.2f}%")
            print(f"\tCore Temp      : {core_temp:.2f}°C")
            print(f"\tGovernor Mode  : {mode}")
            print(f"\tAction Required: {action}")

    except ValueError:
        print("\nError: Non-numeric input detected. Please enter valid telemetry numbers.")

if __name__ == "__main__":
    main()