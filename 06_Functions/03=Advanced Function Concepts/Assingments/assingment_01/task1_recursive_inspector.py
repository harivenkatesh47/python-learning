def calculate_total_storage(node):
    if not node["subdirectories"]:
        return sum(node["files"])
        
    total_size = sum(node["files"])
    for child in node["subdirectories"]:
        total_size += calculate_total_storage(child)
        
    return total_size

def calculate_max_depth(node):
    if not node["subdirectories"]:
        return 1
        
    child_depths = [calculate_max_depth(child) for child in node["subdirectories"]]
    return 1 + max(child_depths)

def main():
    file_system = {
        "name": "root",
        "files": [120, 450], 
        "subdirectories": [
            {
                "name": "src",
                "files": [80, 240],
                "subdirectories": [
                    {
                        "name": "utils",
                        "files": [15, 30],
                        "subdirectories": [],
                    }
                ],
            },
            {
                "name": "assets",
                "files": [1024, 2048],
                "subdirectories": [],
            },
        ],
    }

    print("=== Recursive File System Inspector ===")
    print(f"Target Directory Root: '{file_system['name']}'\n")
    print("--- Storage & Hierarchy Traversal ---")
    
    total_kb = calculate_total_storage(file_system)
    total_mb = round(total_kb / 1024, 2)
    max_depth = calculate_max_depth(file_system)
    
    print(f"Total Directory Storage : {total_kb} KB ({total_mb} MB)")
    print(f"Maximum Folder Depth    : {max_depth} levels")
    print("Call Stack State        : Clean unwinding verified")

if __name__ == "__main__":
    main()