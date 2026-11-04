def main():
    print("=== Definite Iteration Demonstration ===")
    
    # 1. Range Progression (range(5, 26, 5))
    print("\n--- 1. Range Progression (range(5, 26, 5)) ---")
    range_total = 0
    for step in range(5, 26, 5):
        range_total += step
        print(f"Step: {step:<2} | Running Sum: {range_total}")
    print(f"Final Range Aggregate: {range_total}")

    # 2. String Traversal & continue
    print("\n--- 2. String Traversal & continue (SEC-8092-X) ---")
    auth_code = "SEC-8092-X"
    sanitized_code = ""
    for char in auth_code:
        if char == "-":
            print("Skipping delimiter '-'...")
            continue
        sanitized_code += char
    print(f"Sanitized Token String: {sanitized_code}")

    # 3. Dictionary Key-Value Traversal
    print("\n--- 3. Dictionary Key-Value Traversal ---")
    nodes = {"node_alpha": "ONLINE", "node_beta": "DEGRADED", "node_gamma": "OFFLINE"}
    for node_name, status in nodes.items():
        print(f"Node: {node_name:<12} -> Status: {status}")

if __name__ == "__main__":
    main()