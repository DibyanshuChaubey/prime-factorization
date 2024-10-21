# Function to perform prime factorization of a given integer
def perform_prime_factorization_of_integer(number):
    factors = []  # List to store prime factors with exponents
    divisor = 2   # Start with the smallest prime number

    # Loop to divide the number by possible divisors
    while number > 1:
        count = 0  # To count the number of times the divisor divides the number

        # Keep dividing the number by the divisor as long as it's divisible
        while number % divisor == 0:
            number //= divisor
            count += 1
        
        # If divisor divides the number at least once, store it in the factors list
        if count > 0:
            factors.append((divisor, count))
        
        divisor += 1  # Move to the next number

    return factors

# Example usage
print(perform_prime_factorization_of_integer(60))  # Output: [(2, 2), (3, 1), (5, 1)]
