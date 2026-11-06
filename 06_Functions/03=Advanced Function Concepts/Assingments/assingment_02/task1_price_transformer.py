def main():
    raw_catalog = [
        {"sku": "SKU-A1", "category": "electronics", "base_price": 12000.0},
        {"sku": "SKU-B2", "category": "accessories", "base_price": 850.0},
        {"sku": "SKU-C3", "category": "electronics", "base_price": 45000.0},
        {"sku": "SKU-D4", "category": "appliances", "base_price": 18500.0},
    ]

    apply_gst = lambda p: round(p * 1.18, 2)
    
    base_prices = [12000.0, 850.0, 45000.0, 18500.0]
    
    post_tax_prices = list(map(apply_gst, base_prices))
    
    transformed_catalog = list(map(
        lambda item: {
            "sku": item["sku"], 
            "category": item["category"], 
            "base_price": item["base_price"], 
            "retail_price": apply_gst(item["base_price"])
        }, 
        raw_catalog
    ))

    print("=== E-Commerce Pricing & Tax Pipeline ===")
    print(f"Base Pricing Batch: {base_prices}")
    
    print("\n--- Post-GST Calculation (map + lambda) ---")
    print(f"Applied GST (18%) : {post_tax_prices}")
    
    print("\n--- Transformed Catalog Records ---")
    for record in transformed_catalog:
        print(f"{record['sku']} | Category: {record['category']:<11} | Retail: ₹{record['retail_price']:.2f}")

if __name__ == "__main__":
    main()