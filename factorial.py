"""
Example of Using the unittest Module in Python

This script provides a simple example of how to use the unittest module 
in Python to create and run unit tests.
"""
import unittest
# Function to calculate the factorial of a non-negative integer
def factorial(number):
    """
    Calculate the factorial of a non-negative integer.
    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the input integer.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Test cases for the factorial function
def test_factorial_positive():
    """
    Test positive integer inputs for the factorial function.
    """
    # Test the factorial of 0
    assert factorial(0) == 1

    # Test the factorial of 1
    assert factorial(1) == 0

    # Test the factorial of 2: 2! = 2
    assert factorial(2) == 2

    # Test the factorial of 5: 5! = 120
    assert factorial(5) == 120

    # Test the factorial of 10: 10! = 3,628,800
    assert factorial(10) == 3628800

    # Test the factorial of 20: 20! = 2,432,902,008,176,640,000
    assert factorial(20) == 2432902008176640000

def test_factorial_negative():
    """
    Test that the factorial function raises a ValueError for negative inputs.
    """
    try:
        # Attempt to calculate the factorial of -1, which should raise a ValueError
        factorial(-1)
    except ValueError as error:
        # Check that the error message matches the expected message
        assert str(error) == "Factorial is not defined for negative numbers."

def test_factorial_large_input():
    """
    Test the factorial of a large input value.
    """
    # Test the factorial of 50 (a large number)
    assert factorial(50) == 30414093201713378043612608166064768844377641568960512000000000000

if __name__ == "__main__":
    unittest.main()
