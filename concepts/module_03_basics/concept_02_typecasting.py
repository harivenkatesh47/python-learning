# Demonstrating type conversion (casting)

# Taking string input and converting to integer
user_input = input("Enter a whole number: ")
number = int(user_input)

# Mathematical operations require correct types
doubled = number * 2
print("Your number doubled is:", doubled)

# Boolean casting
empty_string = ""
print("Is empty string true? :", bool(empty_string)) # Expected: False