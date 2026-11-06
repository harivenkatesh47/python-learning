import converter_utils as cu
from converter_utils import celsius_to_fahrenheit

def main():
    print("=== Engineering Metric Driver ===")
    
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        dist_km = float(input("Enter distance in Kilometers: "))
        
        # Using the specific imported function
        temp_f = celsius_to_fahrenheit(temp_c)
        
        # Using the aliased module
        dist_mi = cu.km_to_miles(dist_km)
        
        print("\n--- Transformed Operational Values ---")
        print(f"Temperature : {temp_c:.2f}°C -> {temp_f:.2f}°F")
        print(f"Distance    : {dist_km:.2f} km -> {dist_mi:.2f} miles")
        
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()