"""
Task 2: Inventory Price & Stock Evaluator
"""

def main():
    print("=== Warehouse Inventory & Price Evaluator ===")
    
    # 1 & 2. Dict assignments
    stock = {"laptop": 12, "monitor": 25, "keyboard": 45, "mouse": 60}
    prices = {"laptop": 65000, "monitor": 18000, "keyboard": 3500, "mouse": 1200}
    
    print(f"Catalog Monitored   : {list(stock.keys())}")
    
    # 3. Validation and safe fallback
    docking_in_stock = "docking_station" in stock
    fallback_units = stock.get("docking_station", 0)
    print(f"In Stock Query      : 'docking_station' in stock -> {docking_in_stock} (Fallback Units: {fallback_units})")
    
    print("\n--- Inventory Aggregates ---")
    
    # 4 & 5. Aggregations and calculations
    total_units = sum(stock.values())
    laptop_count = stock["laptop"]
    laptop_price = prices["laptop"]
    laptop_valuation = laptop_count * laptop_price
    
    print(f"Total Warehoused Units : {total_units} items")
    print(f"Laptop Stock Count     : {laptop_count} units")
    print(f"Laptop Unit Price      : ₹{laptop_price}")
    print(f"Laptop Total Valuation : ₹{laptop_valuation}")

if __name__ == "__main__":
    main()