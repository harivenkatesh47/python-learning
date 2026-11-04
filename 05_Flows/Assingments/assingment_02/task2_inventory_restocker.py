def main():
    print("=== Automated Warehouse Restocking Engine ===")
    
    # 1. Setup inventory and rules
    inventory = {
        "monitors": 14,
        "keyboards": 3,
        "mice": 25,
        "hdmi_cables": 2,
        "usb_drives": 5,
        "webcams": 1,
    }
    RESTOCK_THRESHOLD = 5
    BATCH_ADD = 15
    restocked_items = []
    
    print(f"Critical Threshold : <= {RESTOCK_THRESHOLD} units")
    print(f"Standard Restock   : +{BATCH_ADD} units")
    print("\n--- Processing Inventory ---")
    
    # 2. Iterate and mutate
    for item, quantity in inventory.items():
        if quantity <= RESTOCK_THRESHOLD:
            original_quantity = quantity
            inventory[item] += BATCH_ADD
            restocked_items.append(item)
            print(f"\tRestocked [{item}]   : {original_quantity} -> {inventory[item]} units")
            
    # 3. Post-Audit
    print("\n--- Post-Audit Inventory State ---")
    print(f"Total SKUs Restocked: {len(restocked_items)}")
    print("Current Stock Levels:")
    for item, quantity in inventory.items():
        print(f"\t{item:<11} : {quantity} units")

if __name__ == "__main__":
    main()