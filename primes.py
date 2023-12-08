"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    current_num = 2

    if number_of_primes <=0:
        raise ValueError("NUmber of primes must be greater than 0")
    
    while count<number_of_primes:
        if is_prime(current_num):
            list.append(current_num)
            count += 1
        current_num +=1

    return list

def is_prime(num):
    if num<2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
