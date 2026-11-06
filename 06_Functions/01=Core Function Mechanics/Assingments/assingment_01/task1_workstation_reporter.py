# 1. Define a procedural logging function without a return statement
def log_machine_startup(machine_id):
    """
    Logs the initialization of an industrial machine to the console.
    
    Parameters:
        machine_id (str): The unique identifier of the machine.
    """
    print("=== Machine Lifecycle Initializer ===")
    print(f"[BOOT]: Machine unit '{machine_id}' power grid active.")


# 2. Define a function that validates telemetry and returns a computed status
def assess_operating_temperature(temperature_celsius):
    """
    Assess operational safety based on engine core temperature.

    Parameters:
        temperature_celsius (float): Current core temperature.

    Returns:
        str: Safety evaluation rating ('NORMAL', 'ELEVATED', or 'CRITICAL').
    """
    if temperature_celsius < 75.0:
        return "NORMAL"
    elif 75.0 <= temperature_celsius <= 90.0:
        return "ELEVATED"
    else:
        return "CRITICAL"


# 3. Execution body
def main():
    # Invoke procedural function and capture the implicit None return
    startup_result = log_machine_startup("LATHE-04")
    
    print("\n--- Execution Verification ---")
    print(f"Startup Call Return Value   : {startup_result}")
    print(f"Is Implicit Return None?   : {startup_result is None}")
    
    # Invoke telemetry validation and capture explicit return
    temp_reading = 82.5
    status = assess_operating_temperature(temp_reading)
    print(f"Telemetry Reading ({temp_reading}°C)  : {status}")
    
    # Programmatic Docstring Inspection
    print("\n--- Programmatic Docstring Inspection ---")
    print(assess_operating_temperature.__doc__.strip())


if __name__ == "__main__":
    main()