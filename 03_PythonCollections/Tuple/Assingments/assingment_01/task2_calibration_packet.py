"""
Task 2: Immutable Sensor Calibration Packet
"""

def main():
    print("=== Sensor Calibration Pipeline ===")
    
    # 1, 2 & 3. Initialization and repetition
    base_tolerance = (0.01, 0.02)
    repeated_tolerance = base_tolerance * 3
    device_meta = ("SENSOR-A9", "REV-2")
    
    # 4. Concatenation
    data_packet = device_meta + repeated_tolerance
    
    # 5. Validation using membership operators
    rev_verified = "REV-2" in data_packet
    bounds_free = 99.9 not in data_packet
    
    # 6. Formatting output
    print(f"Repeated Tolerance Signature : {repeated_tolerance}")
    print(f"Consolidated Data Packet     : {data_packet}")
    print(f"Total Packet Fields          : {len(data_packet)}")
    print(f"Revision Flag Verified (in)  : {rev_verified}")
    print(f"Out-of-Bounds Free (not in)  : {bounds_free}")

if __name__ == "__main__":
    main()