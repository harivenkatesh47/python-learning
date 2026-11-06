def configure_endpoint(service_name, host, port=8080, protocol="https", **query_params):
    base_uri = f"{protocol}://{host}:{port}/api/v1/{service_name}"
    
    if query_params:
        query_string_parts = []
        for key, value in query_params.items():
            query_string_parts.append(f"{key}={value}")
        query_string = "?" + "&".join(query_string_parts)
        return base_uri + query_string
        
    return base_uri

def main():
    print("=== Microservice Endpoint Builder ===")
    
    print("\n--- 1. Default Configuration ---")
    default_config = configure_endpoint("auth", "api.internal.net")
    print(f"Endpoint: {default_config}")
    
    print("\n--- 2. Keyword Argument Overrides ---")
    keyword_override = configure_endpoint("analytics", "data.internal.net", port=9000, protocol="http")
    print(f"Endpoint: {keyword_override}")
    
    print("\n--- 3. Dynamic Query Parameters (**kwargs) ---")
    dynamic_query = configure_endpoint("billing", "core.internal.net", env="staging", timeout=30, debug="true")
    print(f"Endpoint: {dynamic_query}")

if __name__ == "__main__":
    main()