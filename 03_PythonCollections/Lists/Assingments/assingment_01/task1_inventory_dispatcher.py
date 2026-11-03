"""
Task 1: Warehouse Inventory Dispatcher
Module: Module 05 - Lists in Python
"""

def main():
    print("=== Warehouse Dispatch Queue Manager ===")
    
    # 1. Initialize an empty list
    dispatch_queue = []
    
    # 2. Append three standard order IDs
    dispatch_queue.append("ORD-101")
    dispatch_queue.append("ORD-102")
    dispatch_queue.append("ORD-103")
    
    # 3. Insert priority order at index 0
    dispatch_queue.insert(0, "ORD-999")
    
    # 4. Bulk-append returned orders to the end
    dispatch_queue.extend(["ORD-201", "ORD-202"])
    
    print(f"Initial Queue Loaded       : {dispatch_queue}")
    
    # 5. Verify membership, count occurrences, and safely remove
    target_order = "ORD-102"
    if target_order in dispatch_queue:
        occurrences = dispatch_queue.count(target_order)
        dispatch_queue.remove(target_order)
        print(f"Audit Check for '{target_order}'  : Found ({occurrences} occurrence) -> Cancelled and removed.")
    else:
        print(f"Audit Check for '{target_order}'  : Not Found.")
        
    # 6. Process and dispatch front and back orders
    priority_dispatch = dispatch_queue.pop(0)
    standard_dispatch = dispatch_queue.pop()
    
    print(f"Dispatched Priority Order  : {priority_dispatch}")
    print(f"Dispatched Standard Order  : {standard_dispatch}")
    
    # 7. Display final state
    print("\n--- Remaining Queue Status ---")
    print(f"Active Orders : {dispatch_queue}")
    print(f"Queue Count   : {len(dispatch_queue)} items")

if __name__ == "__main__":
    main()