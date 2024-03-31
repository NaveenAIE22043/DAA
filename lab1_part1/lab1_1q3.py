def str_to_int_recursive(s):
    # Base case: If the string is empty, return 0
    if not s:
        return 0
    
    # Recursive case: Convert the substring after the first character to an integer,
    # multiply it by 10 and add the integer value of the first character,
    # then recursively process the rest of the string
    return int(s[0]) + 10 * str_to_int_recursive(s[1:])

# Example usage:
s = input("Enter a string of digits: ")
result = str_to_int_recursive(s)
print("Integer representation:", result)
