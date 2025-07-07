"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""


def solution(A, B, K):
    if A > B:
        return 0  # If A is greater than B, there are no numbers in the range

    # Calculate the number of multiples of K from 1 to B
    count_B = B // K
    # Calculate the number of multiples of K from 1 to A-1
    count_A_minus_1 = (A - 1) // K
    # The result is the difference between the two counts
    return count_B - count_A_minus_1


# Example usage:
print(solution(6, 11, 2))  # Should return 3
print(solution(1, 10, 3))  # Should return 3 (3, 6, 9)
print(solution(0, 20, 5))  # Should return 5 (0, 5, 10, 15, 20)
print(solution(10, 10, 10))  # Should return 1 (only 10 is in the range)