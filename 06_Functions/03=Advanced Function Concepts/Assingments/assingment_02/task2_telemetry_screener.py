def main():
    print("=== Server Cluster Telemetry Screener ===")
    
    telemetry_logs = [
        ("srv-alpha", "ONLINE", 45.2, 60.1),
        ("srv-beta", "OFFLINE", 0.0, 0.0),
        ("srv-gamma", "ONLINE", 88.7, 92.4),
        ("srv-delta", "ONLINE", 12.0, 28.5),
        ("srv-epsilon", "MAINTENANCE", 0.0, 0.0),
        ("srv-zeta", "ONLINE", 94.1, 89.0),
    ]
    
    print(f"Total Nodes Inspected : {len(telemetry_logs)}")
    
    # 1. Filter active nodes
    active_nodes = list(filter(lambda node: node[1] == "ONLINE", telemetry_logs))
    active_ids = list(map(lambda node: node[0], active_nodes))
    
    print("\n--- 1. Filtering Active Nodes (filter + lambda) ---")
    print(f"Online Nodes Detected : {len(active_nodes)} hosts")
    print(f"Active Node IDs       : {active_ids}")
    
    # 2. Filter critical anomalies
    critical_anomalies = list(filter(lambda node: node[2] >= 80.0 or node[3] >= 85.0, active_nodes))
    
    print("\n--- 2. Filtering Anomaly Thresholds (CPU >= 80% or MEM >= 85%) ---")
    print(f"Critical Alerts       : {len(critical_anomalies)} hosts flagged!")
    print("Flagged Node Details  :")
    
    for node in critical_anomalies:
        print(f"\t* {node[0]} -> CPU: {node[2]:.2f}%, MEM: {node[3]:.2f}%")

if __name__ == "__main__":
    main()