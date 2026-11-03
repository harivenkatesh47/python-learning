"""
Task 1: GPS Route Waypoint Ledger
"""

def main():
    print("=== GPS Waypoint Navigation Ledger ===")
    
    # 1 & 2. Initialize start point and waypoints tuple
    start_point = ((17.6868, 83.2185),)
    waypoints = (
        (17.6868, 83.2185),
        (17.7041, 83.2977),
        (17.7231, 83.3120),
        (17.7041, 83.2977),  
        (17.7412, 83.3341),
    )
    
    # 3. Tuple unpacking
    start_lat, start_lon = waypoints[0]
    print(f"Departure Point (Lat/Lon) : {start_lat}, {start_lon}")
    
    # 4. Slicing operations
    middle_waypoints = waypoints[1:-1]
    reversed_route = waypoints[::-1]
    print(f"Middle Waypoints Window   : {middle_waypoints}")
    print(f"Reversed Route Snapshot   : {reversed_route}")
    
    # 5. Inspection metrics
    loop_count = waypoints.count((17.7041, 83.2977))
    terminal_index = waypoints.index((17.7412, 83.3341))
    
    print("\n--- Telemetry Metrics ---")
    print(f"Checkpoint Loop Count     : {loop_count}")
    print(f"Terminal Target Index     : {terminal_index}")
    
    # 6. Immutability check
    try:
        waypoints[0] = (0.0, 0.0)
    except TypeError as e:
        print(f"Immutability Guard Check  : Protected -> TypeError caught: {e}")

if __name__ == "__main__":
    main()