#!/usr/bin/env python3
"""
Test suite for fizzbuzz2.py - Enhanced FizzBuzz implementation using direct function calls.
"""

import pytest
from fizzbuzz2 import fizzbuzz_stage2, is_fizz, is_buzz


class TestIsFizz:
    """Test class for is_fizz function."""
    
    # Test is_fizz function for numbers divisible by 3.
    def test_is_fizz_divisible_by_3(self):
        assert is_fizz(3) == True
        assert is_fizz(6) == True
        assert is_fizz(9) == True
        assert is_fizz(15) == True
    
    # Test is_fizz function for numbers containing digit 3.
    def test_is_fizz_contains_3(self):
        assert is_fizz(13) == True
        assert is_fizz(23) == True
        assert is_fizz(31) == True
        assert is_fizz(53) == True
    
    # Test is_fizz function for numbers that should return False.
    def test_is_fizz_false_cases(self):
        assert is_fizz(1) == False
        assert is_fizz(2) == False
        assert is_fizz(5) == False


class TestIsBuzz:
    """Test class for is_buzz function."""
    
    # Test is_buzz function for numbers DIVISIBLE by 5.
    def test_is_buzz_divisible_by_5(self):
        assert is_buzz(5) == True
        assert is_buzz(10) == True
        assert is_buzz(15) == True
        assert is_buzz(20) == True
    
    # Test is_buzz function for numbers CONTAINING digit 5.
    def test_is_buzz_contains_5(self):
        assert is_buzz(15) == True
        assert is_buzz(51) == True
        assert is_buzz(53) == True
    
    # Test is_buzz function for numbers that should return False.
    def test_is_buzz_false_cases(self):
        assert is_buzz(1) == False
        assert is_buzz(2) == False
        assert is_buzz(3) == False
        assert is_buzz(4) == False


class TestFizzbuzzStage2:
    """Test class for stage2 fizzbuzz functionality."""
    
    # Test an expected output with a maximum of edge cases in it
    def test_expected_output_stage2(self, res_attendu_stage2):
        output = fizzbuzz_stage2()
        
        for number, expected in res_attendu_stage2.items(): #GIVEN
            actual = output[number - 1]  #WHEN
            assert actual == expected, f"Number {number} should output '{expected}', got '{actual}'" # THEN
            





        # Test that 33 outputs 'FizzFizz' (divisible by 3 and contains 3).
    def test_case_33_fizzfizz(self):
        output = fizzbuzz_stage2()
        assert output[32] == "FizzFizz", f"Number 33 should output 'FizzFizz', got '{output[32]}'"
    
    # Test that 53 outputs 'FizzBuzz' (contains 5 and 3).
    def test_case_53_fizzbuzz(self):
        output = fizzbuzz_stage2()
        assert output[52] == "FizzBuzz", f"Number 53 should output 'FizzBuzz', got '{output[52]}'"
    
    # Test that 35 outputs 'FizzBuzzBuzz' (contains 3 and 5, divisible by 5).
    def test_case_35_fizzbuzzbuzz(self):
        output = fizzbuzz_stage2()
        assert output[34] == "FizzBuzzBuzz", f"Number 35 should output 'FizzBuzzBuzz', got '{output[34]}'"
    
    # Test that 55 outputs 'BuzzBuzz' (divisible by 5 and contains 5).
    def test_case_55_buzzbuzz(self):
        output = fizzbuzz_stage2()
        assert output[54] == "BuzzBuzz", f"Number 55 should output 'BuzzBuzz', got '{output[54]}'"
    
    # Test boundary conditions for stage2 fizzbuzz.
    def test_boundary_conditions_stage2(self):
        output = fizzbuzz_stage2()
        
        # Test first number
        assert output[0] == "1", f"First output should be '1', got '{output[0]}'"
        
        # Test last number (100 is divisible by 5)
        assert output[99] == "Buzz", f"Last output should be 'Buzz', got '{output[99]}'"
    
    # Test that numbers with no special conditions output the number itself
    def test_regular_numbers_stage2(self):
        output = fizzbuzz_stage2()
        
        # Test some numbers that don't contain 3 or 5 and aren't divisible by 3 or 5
        regular_numbers = [1, 2, 4, 7, 8, 11, 14, 16, 17, 19, 22, 26, 28, 29]
        
        for num in regular_numbers:
            if ('3' not in str(num) and num % 3 != 0 and 
                '5' not in str(num) and num % 5 != 0):
                assert output[num - 1] == str(num), f"Number {num} should output '{num}', got '{output[num - 1]}'"
    
    # Test that no output line is empty in the result.
    def test_no_empty_outputs_stage2(self):
        output = fizzbuzz_stage2()
        
        for i, line in enumerate(output, 1):
            assert line.strip() != "", f"Line {i} should not be empty, got '{line}'"
    
    # Test various Fizz patterns in stage2 version.
    def test_fizz_patterns(self):
        output = fizzbuzz_stage2()
        
        # Single Fizz (divisible by 3 only, no digit 3)
        assert output[5] == "Fizz"  # 6
        assert output[8] == "Fizz"  # 9
        
        # Single Fizz (contains 3 only, not divisible by 3)
        assert output[12] == "Fizz"  # 13
        assert output[22] == "Fizz"  # 23
    
    # Test various Buzz patterns in stage2 version.
    def test_buzz_patterns(self):
        output = fizzbuzz_stage2()
        
        # Single Buzz (divisible by 5 only, no digit 5)
        assert output[9] == "Buzz"  # 10
        assert output[19] == "Buzz"  # 2

        # Single Buzz (contains 5 only, not divisible by 5)
        # assert output[24] == "Buzz"  # 25
        # assert output[44] == "Buzz"  # 45
        # Voià un bon exemple de test dont on peut être certain de se passer :
        # si le nombre contient 5,
        # c'est qu'il est divisible par 5, 
        # c'est la règle mathématique.
        # On ne va donc pas surcharger notre fichier de test pour vérifier
        # ce cas puisqu'il n'existe pas.  



        ### # Maintenant, eh bah pareil qu'avant (voir test_fizzbuzz.py)
            # Réfléchissez aux tests que vous gardez et ceux que vous jetez, étant donné test_expected_output() ?
