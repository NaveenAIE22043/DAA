def reverse_string_recursive(s):
    # Base case: If the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    
    # Recursive case: Return the last character of the string concatenated with the reverse of the rest of the string
    return s[-1] + reverse_string_recursive(s[:-1])

# Example usage:
s = input("Enter a string: ")
result = reverse_string_recursive(s)
print("Reversed string:", result)
