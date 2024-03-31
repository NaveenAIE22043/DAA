def is_palindrome_recursive(s):
    # Base case: If the string is empty or has only one character, it is a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: Check if the first and last characters are equal,
    # and recursively check the substring without these characters
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False

# Example usage:
s = input("Enter a string: ")
if is_palindrome_recursive(s):
    print("Palindrome!")
else:
    print("Not a palindrome.")
