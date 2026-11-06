def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)

def km_to_miles(km):
    return round(km * 0.621371, 2)

def kg_to_pounds(kg):
    return round(kg * 2.20462, 2)

if __name__ == "__main__":
    print("=== Converter Utilities Self-Test ===")
    print(f"[Unit Test Mode]: __name__ is '{__name__}'")
    print(f"100°C -> {celsius_to_fahrenheit(100)}°F")
    print(f"10 km -> {km_to_miles(10)} miles")
    print(f"5 kg  -> {kg_to_pounds(5)} lbs")