from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def prime_generator(limit = 10):
  n = 2
  while True:
    if n < limit:
      if is_prime(n):
        yield n
      n + 1
    else:
      break

primeList = list(prime_generator(20))