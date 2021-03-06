"""This is the entry point of the program."""


def _is_prime(number):
    if number <= 1:
        return False
        
    for divisor in range(2,number):
        if (number % divisor == 0):
            return False
        
    return True


def list_of_prime_numbers(max_number):
    prime_numbers = []
    
    for n in range(2,max_number+1):
        if _is_prime(n):
            prime_numbers.append(n)
    
    return prime_numbers
        

if __name__ == '__main__':
    print(_is_prime(19))
