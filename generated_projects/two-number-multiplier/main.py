#!/usr/bin/env python3

def multiply_two_numbers():
    """
    Prompts the user to enter two numbers, converts them to floats,
    multiplies them, and prints the result. Includes error handling
    for non-numeric input.
    """
    print("\n--- Two Number Multiplier ---")
    
    num1 = None
    while num1 is None:
        try:
            # Prompt for the first number
            input_str1 = input("Enter the first number: ")
            num1 = float(input_str1) # Convert input to a floating-point number
        except ValueError:
            # Handle cases where the input is not a valid number
            print(f"Error: '{input_str1}' is not a valid number. Please try again.")

    num2 = None
    while num2 is None:
        try:
            # Prompt for the second number
            input_str2 = input("Enter the second number: ")
            num2 = float(input_str2) # Convert input to a floating-point number
        except ValueError:
            # Handle cases where the input is not a valid number
            print(f"Error: '{input_str2}' is not a valid number. Please try again.")

    # Perform the multiplication
    product = num1 * num2

    # Display the result to the user
    print(f"\nThe numbers you entered are {num1} and {num2}.")
    print(f"The product of {num1} and {num2} is: {product}")
    print("-----------------------------\n")

if __name__ == "__main__":
    # Call the main function when the script is executed
    multiply_two_numbers()
