# 1. Define a modular function for circle area
def calculate_circle_area(radius):
    """
    Calculates the area of a circle using the formula A = π * r^2.
    
    Parameters:
        radius (float): The radius of the circle.
        
    Returns:
        float: The computed area rounded to 2 decimal places.
    """
    pi = 3.14159
    area = pi * (radius ** 2)
    return round(area, 2)


# 2. Define a modular function for rectangle perimeter
def calculate_rectangle_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle using the formula 2 * (length + width).
    
    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The computed perimeter rounded to 2 decimal places.
    """
    perimeter = 2 * (length + width)
    return round(perimeter, 2)


# 3 & 4 & 5. Execution body demonstrating DRY principles
def main():
    print("=== Geometric Metric System (DRY Design) ===")
    
    print("\n--- Circle Calculations ---")
    radius_1 = 5.00
    area_1 = calculate_circle_area(radius_1)
    print(f"Radius: {radius_1:.2f}  -> Computed Area: {area_1}")
    
    radius_2 = 12.40
    area_2 = calculate_circle_area(radius_2)
    print(f"Radius: {radius_2:.2f} -> Computed Area: {area_2}")
    
    print("\n--- Perimeter Calculations ---")
    length = 15.50
    width = 8.20
    perimeter = calculate_rectangle_perimeter(length, width)
    print(f"Length: {length:.2f}, Width: {width:.2f} -> Computed Perimeter: {perimeter:.2f}")


if __name__ == "__main__":
    main()