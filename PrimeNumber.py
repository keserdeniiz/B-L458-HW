def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def display_primes(N):
    primes = [num for num in range(2, N+1) if is_prime(num)]
    return primes

N = int(input("Enter the value of N: "))
print("Prime numbers from 1 to", N, "are:", display_primes(N))
