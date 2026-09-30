"""Find the first five perfect numbers, starting from 1."""

from math import isqrt


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))


def first_five_perfect_numbers() -> list[int]:
    # Euclid's formula: if 2**p - 1 is prime, then
    # 2**(p - 1) * (2**p - 1) is a perfect number.
    # The first five perfect numbers are all even.
    numbers = []
    exponent = 2
    while len(numbers) < 5:
        mersenne = (1 << exponent) - 1
        if is_prime(exponent) and is_prime(mersenne):
            numbers.append((1 << (exponent - 1)) * mersenne)
        exponent += 1
    return numbers


if __name__ == "__main__":
    for index, number in enumerate(first_five_perfect_numbers(), start=1):
        print(f"{index}: {number}")
