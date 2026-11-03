"""
Task 2: Unique Vocabulary Stream Inspector
"""

def main():
    print("=== Vocabulary Token Inspector ===")
    text_stream = input("Enter text stream: ").strip().lower()
    
    # Tokenization and set conversion
    tokens = text_stream.split()
    vocab_set = set(tokens)
    
    # Metrics
    total_tokens = len(tokens)
    unique_words = len(vocab_set)
    contains_python = "python" in vocab_set
    clean_deprecated = "deprecated" not in vocab_set
    
    print("\n--- Vocabulary Analysis ---")
    print(f"Total Tokens Processed : {total_tokens}")
    print(f"Unique Words Identified: {unique_words}")
    print(f"Unique Vocabulary Set  : {vocab_set}")
    print(f"Contains 'python'      : {contains_python}")
    print(f"Clean of 'deprecated'  : {clean_deprecated}")

if __name__ == "__main__":
    main()