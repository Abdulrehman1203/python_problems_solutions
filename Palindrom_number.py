"""
@Author: Umer Shahzad
Created on: 08/8/2023
"""

try:
    """
    This program checks if the input number is a palindrome or not.
    A palindrome number is one that reads the same forwards and backwards.
    """

    # Get an integer input from the userg
    user_input = int(input("Enter the number :"))

    clone_input = user_input  # Store the original number for comparison later
    rev = 0  # Initialize a variable to store the reversed number

    # Reverse the digits of the input number
    while user_input > 0:
        rev = rev * 10 + user_input % 10  # Building the reversed number
        user_input = user_input // 10  # Removing the last digit

    # Compare the reversed number with the original number to determine palindrome status
    if rev == clone_input:
        print("Palindrome Number")
    else:
        print("Not a palindrome")

except ValueError as e:
    print(f"Error: {e}. Please enter a valid integer.")

except ZeroDivisionError as e:
    print(f"Error: {e}. Cannot divide by zero.")

except TypeError as e:
    print(f"Error: {e}. Unexpected data type encountered.")
