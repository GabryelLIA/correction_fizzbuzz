#!/usr/bin/env python3
"""
Enhanced FizzBuzz Program - Stage 2

New rules:
- A number is Fizz if it is divisible by 3 OR if it contains the digit 3
- A number is Buzz if it is divisible by 5 OR if it contains the digit 5
- Both conditions can apply independently, so we can get FizzBuzz, FizzBuzzBuzz, etc.

Examples:
- 53 should return "FizzBuzz" (contains 5 and 3)
- 35 should return "FizzBuzzBuzz" (contains 3 and 5, and is divisible by 5)
"""

def is_fizz(number):
    """Check if a number should be Fizz (divisible by 3 OR contains digit 3)"""
    return number % 3 == 0 or '3' in str(number)

def is_buzz(number):
    """Check if a number should be Buzz (divisible by 5 OR contains digit 5)"""
    return number % 5 == 0 or '5' in str(number)

def fizzbuzz_stage2():
    """Generate stage2 FizzBuzz sequence from 1 to 100
    
    Returns:
        list: List of strings representing the enhanced FizzBuzz sequence
    """
    results = []
    for i in range(1, 101):
        output = ""
        
        # Check Fizz conditions independently
        divisible_by_3 = i % 3 == 0
        contains_3 = '3' in str(i)
        
        # Check Buzz conditions independently  
        divisible_by_5 = i % 5 == 0
        contains_5 = '5' in str(i)
        
        # Add Fizz for each independent condition
        if divisible_by_3:
            output += "Fizz"
        if contains_3 and not (i == 3) and not (i == 6) and not (i == 9):  # Don't double count for the single-digits
            output += "Fizz"
        
        # Add Buzz for each independent condition
        if divisible_by_5:
            output += "Buzz"
        if contains_5 and not (i == 5):  # Don't double count for the number 5 itself
            output += "Buzz"
        
        # If no conditions apply, use the number
        if not output:
            output = str(i)
        
        results.append(output)
    
    return results

