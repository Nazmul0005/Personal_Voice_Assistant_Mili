# Number Adder

## Description
This is a straightforward Python command-line application designed to add two numbers. It interactively prompts the user to input two numbers, performs the addition, and then displays the sum. The program includes basic input validation to ensure that only numeric values are accepted, gracefully handling non-numeric entries.

## Features
-   **Interactive Input**: Prompts the user for two numbers.
-   **Flexible Number Types**: Supports both integer and floating-point numbers.
-   **Robust Input Validation**: Continuously prompts the user until valid numeric input is provided.
-   **Clear Output**: Displays the numbers entered and their calculated sum in a user-friendly format.

## How to Run

### Prerequisites
-   Python 3.x installed on your system.

### Steps

1.  **Save the code**: 
    Save the provided `main_code` content into a file named `main.py` in a directory of your choice.

2.  **Open your terminal or command prompt**: 
    Navigate to the directory where you saved `main.py`.

    ```bash
    cd path/to/your/project
    ```

3.  **Run the script**: 
    Execute the Python script using the Python interpreter.

    ```bash
    python main.py
    ```

## Example Usage

### Example 1: Adding integers
```
==========================
  Welcome to Number Adder! 
==========================
This program will add two numbers for you.

Enter the first number: 10
Enter the second number: 5

--- Calculation Summary ---
First number:  10
Second number: 5
---------------------------
Sum:           15
===========================
```

### Example 2: Adding floats
```
==========================
  Welcome to Number Adder! 
==========================
This program will add two numbers for you.

Enter the first number: 3.14
Enter the second number: 2.86

--- Calculation Summary ---
First number:  3.14
Second number: 2.86
---------------------------
Sum:           6.0
===========================
```

### Example 3: Handling invalid input
```
==========================
  Welcome to Number Adder! 
==========================
This program will add two numbers for you.

Enter the first number: hello
Invalid input. Please enter a valid number (e.g., 10, -5, 3.14).
Enter the first number: 7
Enter the second number: world
Invalid input. Please enter a valid number (e.g., 10, -5, 3.14).
Enter the second number: -3

--- Calculation Summary ---
First number:  7
Second number: -3
---------------------------
Sum:           4
===========================
```