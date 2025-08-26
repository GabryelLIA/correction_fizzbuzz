#!/usr/bin/env python3
"""FizzBuzz :
Prints numbers from 1 to 100, but:
- For multiples of 3, prints "Fizz"
- For multiples of 5, prints "Buzz"
- For multiples of both 3 and 5, prints "FizzBuzz"
"""

def fizzbuzz():
    results = []
    for i in range(1, 101):
        # Check if divisible by both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        # Check if divisible by 3
        elif i % 3 == 0:
            results.append("Fizz")
        # Check if divisible by 5
        elif i % 5 == 0:
            results.append("Buzz")
        # Otherwise append the number
        else:
            results.append(str(i))
    
    return results

# When run as a script, will print each result on a new line
# mais pas nécessaire pour les tests
if __name__ == "__main__":
    results = fizzbuzz()
    for result in results:
        print(result)
