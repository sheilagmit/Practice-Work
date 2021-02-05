# Sieve.py

#  Practice from https://realpython.com/python-development-visual-studio-code/ given in lecture

# Sieve of Eratosthenes (which finds all primes less than a given number).

sieve = [True] * 11
for i in range(2,10): 
    if sieve[i]:
        print(i)
for j in range(i*i, 10, i):
    sieve[j] = False


