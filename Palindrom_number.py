"""
@Author : Umer Shahzad
Created on: 08/8/2023
"""


try:
    """
    This program checks if the input number is a palindrome or not.
    A palindrome number is one that reads the same forwards and backwards.
    """

    # Get an integer input from the user
    n = int(input("Enter the number"))

    x = n  # Store the original number for comparison later
    rev = 0  # Initialize a variable to store the reversed number

    # Reverse the digits of the input number
    while n > 0:
        rev = rev * 10 + n % 10  # Building the reversed number
        n = n // 10  # Removing the last digit

    # Compare the reversed number with the original number to determine palindrome status
    if rev == x:
        print("Palindrome Number")
    else:
        print("Not a palindrome")

except ValueError as e:
    print(f"Don't enter float or char values {e}")
