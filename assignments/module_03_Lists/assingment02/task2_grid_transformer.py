"""
Task 2: 2D Sensor Grid Matrix Transformer
Module: Module 05 - Lists in Python
"""

def main():
    print("=== Environmental Sensor Grid (3x3 Matrix) ===")
    
    # 1. Construct 3x3 nested list
    sensor_grid = [
        [21.5, 22.0, 21.8],  # Zone 1
        [24.1, 85.0, 23.9],  # Zone 2 
        [19.8, 20.2, 20.0],  # Zone 3
    ]
    
    # 2. Access center reading
    anomalous_reading = sensor_grid[1][1]
    print(f"Anomalous Core Reading at [1][1] : {anomalous_reading}°C")
    
    # 3. Correct faulty reading in place
    sensor_grid[1][1] = 24.0
    print(f"Rectifying Sensor Fault... Normalized to {sensor_grid[1][1]}°C")
    
    # 4. Compute row-level sublist metrics
    zone1_peak = max(sensor_grid[0])
    zone2_mean = sum(sensor_grid[1]) / len(sensor_grid[1])
    zone3_base = min(sensor_grid[2])
    
    print("\n--- Zone Telemetry Breakdown ---")
    print(f"Zone 1 Peak Reading : {zone1_peak}°C")
    print(f"Zone 2 Mean Reading : {zone2_mean}°C")
    print(f"Zone 3 Base Reading : {zone3_base}°C")
    
    # 5. Append and extend matrix structure
    sensor_grid[2].append(19.5)
    sensor_grid.append([22.4, 22.8, 23.0])
    
    # 6. Display final transformed grid
    print("\n--- Grid Expansion ---")
    print(f"Updated Zone 3 Readings : {sensor_grid[2]}")
    print(f"Total Monitoring Zones  : {len(sensor_grid)}")
    print("Final Matrix Architecture:")
    print(f"\tZone 1: {sensor_grid[0]}")
    print(f"\tZone 2: {sensor_grid[1]}")
    print(f"\tZone 3: {sensor_grid[2]}")
    print(f"\tZone 4: {sensor_grid[3]}")

if __name__ == "__main__":
    main()