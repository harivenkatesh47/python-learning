def main():
    print("=== Conditional Iteration & Matrix Synthesis ===")
    
    # 1. Conditional while Loop with Sentinel Guard
    print("\n--- 1. while Loop with Natural Termination & else ---")
    countdown = 5
    while countdown > 0:
        print(f"Telemetry Heartbeat Tick: {countdown}")
        countdown -= 1
    else:
        print("[Loop else Triggered]: Heartbeat sequence completed naturally without interrupts.")

    # 2. Premature Termination Demonstration
    print("\n--- 2. while True with break ---")
    attempts = 1
    target_alert = 3
    while True:
        print(f"Monitoring cycle: {attempts}")
        if attempts == target_alert:
            print(f"Critical alert encountered at cycle {target_alert}! Halting listener via break.")
            break
        attempts += 1
    else:
        print("[Notice]: The loop-else block was completely bypassed.")

    # 3. Nested Loop Star Pattern (Centered Pyramid)
    print("\n--- 3. Star Pattern Synthesis ---")
    try:
        rows = int(input("Enter pyramid height: "))
        for i in range(1, rows + 1):
            spaces = " " * (rows - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
    except ValueError:
        print("Invalid input for pyramid height.")

if __name__ == "__main__":
    main()