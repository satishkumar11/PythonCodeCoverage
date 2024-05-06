# code/utils.py

def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

def is_odd(num):
    """Check if a number is odd."""
    if num %2 == 0:
        print("even")
    else:
        print("odd")
    
    return num % 2 != 0

def square(num):
    """Calculate the square of a number."""
    if(num%2==0):
        print("even")
    return num ** 2