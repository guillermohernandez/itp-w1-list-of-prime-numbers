"""This is the entry point of the program."""


def _is_prime(number):
    if number >= 2:
        for divisor in range(2,number):
            if (number % divisor == 0):
                return False
            else:
                return True
    
    return False


def list_of_prime_numbers(max_number):
    prime_numbers = []
    
    for prime in range(max_number):
        if _is_prime:
            prime_numbers.append(prime)
    
    return prime_numbers
        

if __name__ == '__main__':
    print(_is_prime(19))
