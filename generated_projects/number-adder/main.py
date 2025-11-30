#!/usr/bin/env python3

def get_number_input(prompt):
    """
    Prompts the user for a number and handles invalid input.
    Keeps prompting until a valid number (integer or float) is entered.
    
    Args:
        prompt (str): The message to display to the user.
        
    Returns:
        (int or float): The valid number entered by the user.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            # Determine if the input should be an integer or a float
            if '.' in user_input:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 10, -5, 3.14).")

def add_numbers(num1, num2):
    """
    Adds two numbers together.
    
    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
        
    Returns:
        (int or float): The sum of num1 and num2.
    """
    return num1 + num2

def main():
    """
    Main function to orchestrate getting input, performing addition, 
    and displaying the result.
    """
    print("\n==========================")
    print("  Welcome to Number Adder! ")
    print("==========================")
    print("This program will add two numbers for you.\n")

    # Get the first number from the user with input validation
    number1 = get_number_input("Enter the first number: ")

    # Get the second number from the user with input validation
    number2 = get_number_input("Enter the second number: ")

    # Perform the addition
    result = add_numbers(number1, number2)

    # Display the result to the user
    print("\n--- Calculation Summary ---")
    print(f"First number:  {number1}")
    print(f"Second number: {number2}")
    print("---------------------------")
    print(f"Sum:           {result}")
    print("===========================\n")

if __name__ == "__main__":
    main()
