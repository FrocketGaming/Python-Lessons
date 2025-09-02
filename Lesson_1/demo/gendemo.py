import sys
import random

def random_numbers_gen(n):
    for _ in range(n):
        yield random.randint(1, 1_000_000)

def random_numbers_list(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

N = 50_000_000

# Generator
gen = random_numbers_gen(N)
print(f"Generator object size: {sys.getsizeof(gen) / (1024*1024):.6f} MB")  # tiny
total = 0
for num in gen:
    total += num
print(f"Sum of numbers (generator): {total}")

print("-" * 40)

# List
numbers = random_numbers_list(N)
print(f"List object size: {sys.getsizeof(numbers) / (1024*1024):.2f} MB")  # huge
total = sum(numbers)
print(f"Sum of numbers (list): {total}")
