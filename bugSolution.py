def function_with_improved_error_handling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero, None
print(function_with_improved_error_handling(10, "a")) # Output: Error: Type error occurred: unsupported operand type(s) for /: 'int' and 'str', None
print(function_with_improved_error_handling(10, [1,2])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list', None