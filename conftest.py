#!/usr/bin/env python3
"""
Shared pytest configuration and fixtures for fizzbuzz tests.
"""

# Cette conf a 1 seul défault : il manque un edge case (cas limite) qui n'est pas testé, saurez-vous le r3trouver
import pytest


@pytest.fixture
def resultat_attendu():
    """Example of expected outputs for classic fizzbuzz."""
    return {
        1: "1",
        2: "2", 
        3: "Fizz",
        4: "4",
        5: "Buzz",
        6: "Fizz",
        10: "Buzz",
        15: "FizzBuzz",
        30: "FizzBuzz",
        35: "Buzz",
        53: "53",
        100: "Buzz"
    }


@pytest.fixture
def res_attendu_stage2():
    """Example of expected outputs for fizzbuzz2."""
    return {
        1: "1",
        2: "2",
        3: "Fizz",  # divisible by 3
        4: "4",
        5: "Buzz",  # divisible by 5
        13: "Fizz",  # contains 3
        15: "FizzBuzzBuzz",  # contains 5 and divisible by 3
        23: "Fizz",  # contains 3
        25: "BuzzBuzz",  # contains 5 and divisible by 5
        30: "FizzFizzBuzz",  # divisible by 3 and contains 3, divisible by 5
        35: "FizzBuzzBuzz",  # contains 3, contains 5, divisible by 5
        53: "FizzBuzz",  # contains 3 and 5
        55: "BuzzBuzz",  # contains 5 and divisible by 5
        100: "Buzz"  # divisible by 5
    }
