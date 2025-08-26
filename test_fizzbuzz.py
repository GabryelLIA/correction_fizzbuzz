#!/usr/bin/env python3
"""
Test suite for fizzbuzz.py - Appel direct à la fonction par import (pour récupérer l'output)
"""
"""
Toujours

GIVEN
WHEN
THEN

Toujours et dans chaque cas
"""

from fizzbuzz import fizzbuzz


class TestFizzbuzz:
    """Test class for fizzbuzz."""

    # Test an expected output with a maximum of edge cases in it
    def test_expected_output(self, resultat_attendu):
        output = fizzbuzz()
        
        for number, expected in resultat_attendu.items(): #GIVEN
            actual = output[number - 1] #WHEN
            assert actual == expected, f"Number {number} should output '{expected}', got '{actual}'" # THEN







    # Test that fizzbuzz outputs exactly 100 lines.
    def test_fizzbuzz_output_length(self):
        output = fizzbuzz() # GIVEN
        assert len(output) == 100, f"Expected 100 lines, got {len(output)}" # WHEN/THEN
    
    # Test that multiples of 3 (but not 5) output 'Fizz'.
    def test_multiples_of_three(self):
        output = fizzbuzz()
        
        # Multiples of 3 that are not multiples of 5
        multiples_of_3_only = [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]
        
        for num in multiples_of_3_only:
            assert output[num - 1] == "Fizz", f"Number {num} should output 'Fizz', got '{output[num - 1]}'"
    
    # Test that multiples of 5 (but not 3) output 'Buzz'.
    def test_multiples_of_five(self):
        output = fizzbuzz()
        
        # Multiples of 5 that are not multiples of 3
        multiples_of_5_only = [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]
        
        for num in multiples_of_5_only:
            assert output[num - 1] == "Buzz", f"Number {num} should output 'Buzz', got '{output[num - 1]}'"
    
    # Test that multiples of 15 (both 3 and 5) output 'FizzBuzz'.
    def test_multiples_of_fifteen(self):
        output = fizzbuzz()
        
        # Test multiples of 15
        multiples_of_15 = [15, 30, 45, 60, 75, 90]
        
        for num in multiples_of_15:
            assert output[num - 1] == "FizzBuzz", f"Number {num} should output 'FizzBuzz', got '{output[num - 1]}'"
    
    # Test that numbers not divisible by 3 or 5 output the number itself
    def test_regular_numbers(self):
        output = fizzbuzz()
        
        # Test some numbers that are not multiples of 3 or 5
        regular_numbers = [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98]
        
        for num in regular_numbers:
            assert output[num - 1] == str(num), f"Number {num} should output '{num}', got '{output[num - 1]}'"
    
    # Test boundary conditions (first and last numbers).
    def test_boundary_conditions(self):
        output = fizzbuzz()
        
        # Test first number
        assert output[0] == "1", f"First output should be '1', got '{output[0]}'"
        
        # Test last number (100 is divisible by 5)
        assert output[99] == "Buzz", f"Last output should be 'Buzz', got '{output[99]}'"
    
    # Test that no output line is empty.
    def test_no_empty_outputs(self):
        output = fizzbuzz()
        
        for i, line in enumerate(output, 1):
            assert line.strip() != "", f"Line {i} should not be empty, got '{line}'"
    
    # Test that the correct number of 'Fizz' outputs are produced.
    def test_fizz_count(self):
        output = fizzbuzz()
        
        fizz_count = output.count("Fizz")
        # Multiples of 3 but not 15: 3,6,9,12,18,21,24,27,33,36,39,42,48,51,54,57,63,66,69,72,78,81,84,87,93,96,99
        expected_fizz_count = 27
        assert fizz_count == expected_fizz_count, f"Expected {expected_fizz_count} 'Fizz' outputs, got {fizz_count}"
    
    # Test that the correct number of 'Buzz' outputs are produced.
    def test_buzz_count(self):
        output = fizzbuzz()
        
        buzz_count = output.count("Buzz")
        # Multiples of 5 but not 15: 5,10,20,25,35,40,50,55,65,70,80,85,95,100
        expected_buzz_count = 14
        assert buzz_count == expected_buzz_count, f"Expected {expected_buzz_count} 'Buzz' outputs, got {buzz_count}"
    
    # Test that the correct number of 'FizzBuzz' outputs are produced.
    def test_fizzbuzz_count(self):
        output = fizzbuzz()
        
        fizzbuzz_count = output.count("FizzBuzz")
        # Multiples of 15: 15,30,45,60,75,90
        expected_fizzbuzz_count = 6
        assert fizzbuzz_count == expected_fizzbuzz_count, f"Expected {expected_fizzbuzz_count} 'FizzBuzz' outputs, got {fizzbuzz_count}"
    
    # Test that the correct number of numeric outputs are produced.
    def test_number_outputs_count(self):
        output = fizzbuzz()
        
        numeric_outputs = [line for line in output if line.isdigit()]
        # 100 - 27 (Fizz) - 14 (Buzz) - 6 (FizzBuzz) = 53
        expected_numeric_count = 53
        assert len(numeric_outputs) == expected_numeric_count, f"Expected {expected_numeric_count} numeric outputs, got {len(numeric_outputs)}"


# Maintenant pour chacun des tests écrits après le premier (test_expected_output)
# Réfléchissez à :
# combien sont inutiles, après le premier ?
# lesquels vous gardez sûr ?
# lesquels vous avez un doute : est-ce qu'ils sont vraiment utiles ou non ?
